import { useEffect, useState } from "react";

function PomodoroTimer() {
  const [secondsLeft, setSecondsLeft] = useState(25 * 60);
  const [isRunning, setIsRunning] = useState(false);
  const [subject, setSubject] = useState("");

  useEffect(() => {
    if (!isRunning) {
      return;
    }

    if (secondsLeft <= 0) {
      setIsRunning(false);
      return;
    }

    const timer = setInterval(() => {
      setSecondsLeft((previousSeconds) => {
        return previousSeconds - 1;
      });
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, [isRunning, secondsLeft]);

  return (
    <div>
      <h1>Study Timer</h1>
           <input
        type="text"
        placeholder="What are you studying?"
        value={subject}
        onChange={(event) => {
          setSubject(event.target.value);
        }}
      />

      <h2>
        {Math.floor(secondsLeft / 60)}:
        {String(secondsLeft % 60).padStart(2, "0")}
      </h2>

      <button onClick={() => setIsRunning(true)}>Start</button>

      <button onClick={() => setIsRunning(false)}>Pause</button>

      <button
        onClick={() => {
          setIsRunning(false);
          setSecondsLeft(25 * 60);
        }}
      >
        Reset
      </button>

 
    </div>
  );
}

export default PomodoroTimer;
