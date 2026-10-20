# Business Idea Assessment Skill

[![Validate](https://img.shields.io/badge/validation-local%20%2B%20CI-0f766e)](.github/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version: v0.2.1](https://img.shields.io/badge/version-v0.2.1-2563eb)](CHANGELOG.md)

A reusable agent skill for turning an early business idea into a current,
source-bound market and feasibility study, then completing the useful follow-on
work that can be done safely without pretending external validation has occurred.

The skill creates auditable Markdown and CSV deliverables, builds bottom-up
market and financial models, identifies decision gates, drafts validation tools,
and repeats evidence, arithmetic, integration, and clean-room reviews until no
known internal defect remains.

## What it does

- Frames and compares plausible versions of the offer.
- Maps direct competitors and substitutes with observed prices and source dates.
- Models reachable customers, channels, operations, unit economics, cash needs,
  and five-year scenarios without false precision.
- Researches current compliance, technical feasibility, funding, and support.
- Produces risks, routes to market, stop conditions, and a ranked recommendation.
- Executes safe autonomous next steps such as outreach drafts, RFQs, compliance
  preflights, 13-week cash control, test protocols, partner searches, and a
  30/60/90-day plan.
- Runs four review gates and records defects, fixes, and unresolved external
  evidence.

It does **not** send messages, submit applications, spend money, place orders,
publish, or alter external systems without explicit authorization.

## Install

Clone or download this repository and run the commands below from its root.
Install the complete `skills/business-idea-assessment/` directory, not only
`SKILL.md`, because the workflow uses its bundled references and validators.
Review third-party skill instructions before granting an agent access to your
files, shell, browser, or external services.

### Skills CLI (recommended)

After publishing the repository on GitHub, replace `YOUR_GITHUB_USERNAME` and
install the skill globally with:

```bash
npx skills add YOUR_GITHUB_USERNAME/BusinessIdeaAssessmentSkill \
  --skill business-idea-assessment -g
```

To verify discovery without installing it:

```bash
npx skills add YOUR_GITHUB_USERNAME/BusinessIdeaAssessmentSkill --list
```

### Codex, OpenCode, and Pi: one portable location

All three currently discover the open Agent Skills layout under
`.agents/skills/`. For a personal installation available across projects:

```bash
mkdir -p "$HOME/.agents/skills/business-idea-assessment"
cp -R skills/business-idea-assessment/. \
  "$HOME/.agents/skills/business-idea-assessment/"
```

For a project installation that can be committed with that project:

```bash
mkdir -p .agents/skills/business-idea-assessment
cp -R skills/business-idea-assessment/. \
  .agents/skills/business-idea-assessment/
```

- **Codex:** run `/skills` or type `$business-idea-assessment` in a prompt.
  Codex normally detects changes automatically; restart it if the skill does
  not appear. See the official [Codex skill locations and invocation
  guide](https://developers.openai.com/codex/skills#where-codex-loads-local-skills).
- **OpenCode:** start OpenCode inside the project scope and ask it to use the
  `business-idea-assessment` skill. Native alternatives are
  `~/.config/opencode/skills/` for a personal install and `.opencode/skills/`
  for a project install. See the official [OpenCode Agent Skills
  guide](https://opencode.ai/docs/skills/).
- **Pi:** invoke `/skill:business-idea-assessment` to force loading, or describe
  a matching task and let Pi select it. Run `/reload` after editing the skill in
  an active session. See Pi's official [skills
  documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md).

### Claude Code

For a personal installation available across projects:

```bash
mkdir -p "$HOME/.claude/skills/business-idea-assessment"
cp -R skills/business-idea-assessment/. \
  "$HOME/.claude/skills/business-idea-assessment/"
```

For a project installation that can be committed with that project:

```bash
mkdir -p .claude/skills/business-idea-assessment
cp -R skills/business-idea-assessment/. \
  .claude/skills/business-idea-assessment/
```

Invoke `/business-idea-assessment`, or describe a matching assessment task and
allow Claude Code to select it. If a new top-level skills directory was created
during an active session and is not visible, run `/reload-skills`. See the
official [Claude Code skills guide](https://code.claude.com/docs/en/skills).

### Any other agent

If the agent supports the open Agent Skills format, copy the entire
`business-idea-assessment` folder into its documented personal or project skill
directory. The portable contract is the folder plus `SKILL.md`; the
`agents/openai.yaml` file is optional Codex/ChatGPT metadata and is not required
by other hosts.

If the agent does not discover `SKILL.md` packages, attach or expose the skill
folder and begin with this prompt:

```text
Read business-idea-assessment/SKILL.md completely before acting. Treat it as
the workflow instructions for this task. Resolve every relative path from the
business-idea-assessment directory, read the references that SKILL.md routes
you to, and use the bundled validators when your environment can run them.
Then assess this idea: <idea, geography, founders, constraints, and goal>.
```

The full workflow needs current web research, local file creation, and ideally
shell access for validation. An agent missing one of those capabilities should
state the limitation, mark the affected outputs as incomplete, and never imply
that current sources, files, or calculations were verified when they were not.

## Use

Use the host's explicit syntax when available:

| Host | Explicit invocation |
|---|---|
| Codex | `$business-idea-assessment` |
| Claude Code | `/business-idea-assessment` |
| OpenCode | Ask the agent to use the `business-idea-assessment` skill |
| Pi | `/skill:business-idea-assessment` |
| Other agents | Use the generic prompt in the install section |

Full-cycle example:

```text
Use the business-idea-assessment skill to assess a mobile bicycle-repair subscription
for apartment residents in Halifax, Nova Scotia. The founders are two mechanics
at concept stage. Complete the decision-ready study, execute every useful and
safe autonomous next step, and review the package before handoff.
```

The skill also supports narrower modes:

```text
Use the business-idea-assessment skill for an assessment-only study of this idea.
```

```text
Use the business-idea-assessment skill to continue the existing assessment at [path],
complete remaining autonomous work, and rerun the review routine.
```

```text
Use the business-idea-assessment skill to refresh prices, regulations, programs,
and the recommendation in this assessment as of today.
```

## When it asks the user

The workflow avoids needless pauses. It asks at only three meaningful places:

1. **Intake:** when missing jurisdiction, customer, founder constraints, or
   business model would materially change the study.
2. **Strategic/external gate:** when equally plausible routes require a founder
   choice, or immediately before any external action or commitment.
3. **Final decision:** to present `advance`, `revise`, `pause`, or `stop`, the
   next bounded spend, and the evidence required before proceeding.

Evidence, model, and integration reviews run automatically between these user
checkpoints.

## Repository layout

```text
skills/business-idea-assessment/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── assessment-workflow.md
│   ├── autonomous-follow-on.md
│   ├── deliverable-contract.md
│   ├── review-routine.md
│   └── user-checkpoints.md
└── scripts/
    ├── validate_assessment.py
    └── validate_repository.py
```

See the [installable skill](skills/business-idea-assessment/SKILL.md),
[behavioural cases](tests/behavioral_cases.md), and
[contribution guide](CONTRIBUTING.md).

## Validation

The repository has no third-party runtime dependency for validation:

```bash
python3 skills/business-idea-assessment/scripts/validate_repository.py .
python3 skills/business-idea-assessment/scripts/validate_assessment.py --self-test
```

To validate a generated assessment package:

```bash
python3 skills/business-idea-assessment/scripts/validate_assessment.py \
  /path/to/research/YYYY-MM-DD-idea-assessment
```

The validator checks file types, CSV shape, ISO dates, source-URL fields, local
links, and README coverage. It deliberately does not claim to verify market
truth, legal interpretation, arithmetic unique to every model, or the quality
of a cited source; the skill's semantic review gates cover those areas.

## Limitations

This skill produces research and decision support, not legal, accounting,
medical, engineering, safety, investment, or regulatory approval. A complete
desk study cannot prove demand, eligibility, technical performance, supplier
capability, funding, or future business success. Those remain explicit external
evidence gates.

## License

[MIT](LICENSE)

