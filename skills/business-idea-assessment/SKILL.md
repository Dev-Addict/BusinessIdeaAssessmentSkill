---
name: business-idea-assessment
description: Produce a current, source-bound market, feasibility, operating, financial, and validation package for a new business idea, then execute safe autonomous follow-on work and review the package until no known internal defects remain. Use for decision-ready assessment of a commercial idea or autonomous next-step execution; do not use for a quick opinion or to take external actions without authorization.
metadata:
  short-description: Assess and validate a business idea
---

# Business Idea Assessment

Turn an early business idea into an auditable decision package and a bounded
evidence program. Prefer completed Markdown/CSV artifacts over a plan describing
future work.

## Choose the run mode

- **Full cycle:** default when the user supplies an idea without narrowing the
  request. Complete the initial assessment, safe autonomous follow-on work, and
  all review gates.
- **Assessment only:** stop after the decision-ready initial study when the user
  explicitly asks for research only.
- **Continuation:** inspect an existing assessment, identify unresolved work
  that is safe to do autonomously, execute it, and integrate the result.
- **Refresh:** re-verify drift-prone sources, prices, regulations, programs, and
  recommendations as of the current date before rerunning reviews.

## Intake and user checkpoints

Proceed without a question when the idea, initial geography, and intended
customer are reasonably inferable. Ask one compact set of at most three
questions only when an answer would materially change the research, usually:

1. operating/sales geography or regulatory jurisdiction;
2. founder stage, resources, or non-negotiable constraints; and
3. intended customer or business model when multiple interpretations are
   equally plausible.

Do not pause merely to ask for preferences that can be labelled as assumptions.
Read [references/user-checkpoints.md](references/user-checkpoints.md) when facts
are missing, strategic routes are tied, or an external action may be useful.

## Execute the full cycle

1. Create `research/YYYY-MM-DD-<idea-slug>-assessment/` unless the user names a
   destination. Use the user's requested currency; otherwise use the operating
   market's currency and state it.
2. Read [references/assessment-workflow.md](references/assessment-workflow.md)
   and [references/deliverable-contract.md](references/deliverable-contract.md).
   Research and write the initial study. Use current primary sources and direct
   URLs beside material claims.
3. Run the **evidence gate** in
   [references/review-routine.md](references/review-routine.md) before relying on
   collected inputs in financial or success models. Fix defects immediately.
4. Finish the initial study, run the **model and draft gate**, and update the
   recommendation to match the corrected evidence.
5. Read [references/autonomous-follow-on.md](references/autonomous-follow-on.md).
   Rank unresolved next steps, execute every safe and useful autonomous task
   within scope, and place its artifacts under `next_steps/`. Do not stop after
   producing a backlog.
6. Run the **integration gate** across the initial study and follow-on package.
   Repair inconsistencies rather than documenting avoidable defects.
7. Run the **final clean-room gate**. Repeat fix-and-review cycles until no known
   internal defect remains. Preserve external unknowns as explicit validation
   tasks; review cannot turn them into facts.
8. Return a concise executive result, the recommended next human action, the
   key stop conditions, and a link to the root `README.md`.

## Evidence and modelling rules

- Browse for current prices, laws, programs, competitors, standards, market
  conditions, and recommendations. Prefer regulators, governments, industry
  bodies, manufacturers, retailers, and the companies being described.
- Distinguish `observed`, `sourced estimate`, `assumption`, `inference`, and
  `unresolved`. Never convert absence of discovered competition into proof of
  demand.
- Separate total opportunity from realistically obtainable sales. Prefer a
  bottom-up model based on reachable accounts or users, transactions, capacity,
  purchase rates, and repeat behaviour.
- Treat technical feasibility, safety, approvals, customer acceptance, supplier
  capability, funding, and shelf life as unproven until required evidence exists.
- Show formulas and units. Use ranges and scenarios where uncertainty is high.
  Label success probabilities as subjective, evidence-informed judgment—not
  measured startup survival statistics.
- Cite source URLs and access dates. Record inaccessible sources and a practical
  way to close the gap.
- Do not invent survey results, quotes, conversion rates, certifications,
  eligibility, or precise market shares.

## Action boundary

Autonomous work may research, calculate, draft, structure, validate, and create
reversible local files. It may draft outreach, RFQs, applications, labels, test
protocols, and buyer materials, but must mark them as drafts.

Obtain explicit authorization immediately before sending messages, submitting
applications, placing orders, booking services, publishing, opening accounts,
spending money, signing terms, or changing external systems. A request for an
assessment does not authorize those actions.

## Artifact rules

- Default to Markdown and CSV. Use another format only when the user asks.
- Make the root `README.md` link every deliverable and state research date,
  geography, currency, recommendation, confidence, next decision, and limits.
- Give CSVs explicit headers and one unit per numeric column. Use `NA` instead
  of fabricated values.
- Keep assumptions and source observations separately identifiable.
- Run `python3 scripts/validate_assessment.py <assessment-directory>` from this
  skill after each structural review gate. The script proves structural
  invariants only; complete semantic and arithmetic checks from the review
  reference as well.
