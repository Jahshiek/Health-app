# Contributing to NurseFlow

## Branch Strategy

### main
Stable and demo-ready code.

### develop
Integration branch for completed features.

### feature/*
All new features should be built on feature branches created from `develop`.

Examples:

- `feature/fastapi-setup`
- `feature/auth`
- `feature/courses-api`
- `feature/tasks-api`
- `feature/ai-quizzes`

## Workflow

Before starting a new feature:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/feature-name