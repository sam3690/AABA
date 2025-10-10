# Contributing to AABA

Thanks for your interest in helping shape the Autonomous Business Administration Agent! This guide explains how to get started quickly and contribute effectively.

## Code of conduct

By participating, you agree to uphold our shared commitment to respectful collaboration. Be kind, be inclusive, and assume good intent.

## Development setup

1. **Clone and fork** the repository.
2. **Install dependencies**
   - Backend: `cd backend && uv sync`
   - Frontend: `cd frontend && npm install`
3. **Copy** the environment template: `cp .env.example .env`
4. **Run the stack** via Docker Compose (`cd infra && docker compose up`).

## Branching strategy

- Create feature branches from `main` using the pattern `feature/<topic>` or `fix/<topic>`.
- Keep commits focused. Squash locally if necessary before submitting a PR.

## Testing & quality gates

Before opening a pull request:

- `cd backend && uv run pytest`
- `uv run ruff check .`
- `uv run mypy app`
- `uv run black --check app`
- Frontend lint (optional for now): `npm run lint`
- Ensure `docker compose build` completes without errors.

## Pull request checklist

- Provide a clear description of the change and motivation.
- Update documentation, env templates, or config files when introducing new services or variables.
- Reference any relevant issues or discussions.
- Include screenshots or logs for UX and operations changes.

## Review process

Project maintainers will review PRs as quickly as possible. Expect feedback on clarity, tests, docs, and adherence to existing code structure. Iteration is welcome—keep the conversation friendly and constructive.

## Communication

- Use GitHub Issues for bugs and feature requests.
- Start a discussion (or use GitHub Discussions) for architectural proposals or exploratory ideas.

## Thank you!

Your contributions make this project better for everyone. 🙌
