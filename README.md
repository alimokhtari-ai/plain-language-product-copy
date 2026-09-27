# Plain Language Product Copy

[![Validate skill](https://github.com/alimokhtari-ai/plain-language-product-copy/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/alimokhtari-ai/plain-language-product-copy/actions/workflows/validate-skill.yml)

An open Agent Skill for turning dense product, AI, technical, and operational language into clear, trustworthy user-facing English.

It helps agents write product copy people can understand on the first read—without inventing facts, weakening commitments, or talking down to the reader.

## Use it for

- landing pages, navigation, CTAs, forms, and onboarding
- AI and automation product explanations
- empty states, errors, consent, and privacy copy
- release notes and user-facing documentation
- SaaS, analytics, and technical jargon that needs plain English

## Core principle

> Keep the truth. Remove the friction.

## Quick example

**Before**

> Leverage our AI-powered orchestration layer to unlock actionable insights across your operational data estate.

**After**

> Connect your operational data to see what needs attention and decide what to do next.

The simplified version must still be checked against the product's real behavior before it is published.

## Install

### Codex

```bash
npx -y skills add https://github.com/alimokhtari-ai/plain-language-product-copy \
  --skill "plain-language-product-copy" \
  --agent codex \
  --global
```

### Claude Code

```bash
npx -y skills add https://github.com/alimokhtari-ai/plain-language-product-copy \
  --skill "plain-language-product-copy" \
  --agent claude-code \
  --global
```

## What is included

- `SKILL.md` — workflow, guardrails, and output patterns
- `references/quality-gates.md` — clarity, truth, accessibility, and safety checks
- `references/examples.md` — concrete before-and-after rewrites
- `references/term-map.md` — practical replacements for common jargon
- `agents/openai.yaml` — agent interface metadata

## Quality bar

Every rewrite should preserve:

1. factual accuracy and important limitations;
2. the user's ability to make an informed decision;
3. privacy, consent, and accessibility requirements; and
4. the original product intent.

## Project standards

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Open an issue](https://github.com/alimokhtari-ai/plain-language-product-copy/issues/new/choose)

## Status

The `main` branch is validated and packaged by GitHub Actions on every relevant push and pull request.
