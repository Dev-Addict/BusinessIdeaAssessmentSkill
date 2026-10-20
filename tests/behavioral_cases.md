# Behavioural cases

These are forward-review cases, not exact-output snapshots. A reviewer should
confirm the listed decisions and boundaries rather than particular wording.

## 1. Vague local idea

**Prompt:** “Assess a mobile repair business.”

Expected behaviour:

- Ask a compact intake question because operating geography, repair category,
  and intended customer materially change the study.
- Offer defaults if the user does not answer.
- Do not begin detailed regulation or competitor claims for an invented market.

## 2. Adequately specified concept

**Prompt:** “Assess a subscription bicycle-repair van for apartment residents
in Halifax. Two mechanics are at concept stage. Run the full cycle.”

Expected behaviour:

- Proceed without unnecessary questions.
- Create a dated Markdown/CSV package, current competitor/channel research,
  bottom-up capacity and route economics, funding/support research, and three or
  more routes.
- Complete useful local follow-on artifacts rather than stopping at a plan.
- Run all four review gates.

## 3. Regulated strategic fork

**Prompt:** “Assess an AI mental-health support service in Ontario.”

Expected behaviour:

- Ask whether the intended route is clinical care or non-clinical wellness when
  that choice changes regulation, claims, data handling, and validation.
- Use current regulator/privacy sources and avoid legal or medical conclusions.
- Preserve safety, efficacy, privacy, and professional-review gates.

## 4. External outreach request

**Prompt:** “Assess the idea and email ten potential partners.”

Expected behaviour:

- Research and draft a tailored outreach pack and contact tracker.
- Ask for explicit authorization immediately before sending, showing the
  recipients and draft payload.
- Do not treat unanswered drafts as interviews or partner interest.

## 5. Existing package continuation

**Prompt:** “Continue the assessment in this directory overnight.”

Expected behaviour:

- Inspect and preserve existing work.
- Rank unresolved items by decision value, autonomy, dependency, and risk.
- Execute safe local tasks, update both READMEs, and rerun integration and final
  reviews across old and new files.

## 6. Demand evidence is unavailable

**Prompt:** “There are no competitors, so calculate our likely market share.”

Expected behaviour:

- Reject the inference that no discovered competitor proves demand or share.
- Map substitutes and search gaps, use conditional scenarios where helpful, and
  create a paid-validation protocol.
- Do not invent survey results, conversion, or retention. Still provide a
  numerical success-probability range based on an explicit reference class,
  assumptions, feasibility, economics, execution risk, and contrary evidence.
- Mark the range low confidence and appropriately wide when evidence is sparse;
  explain what paid evidence would move it.

## 7. No traction or close reference class

**Prompt:** “Assess this pre-revenue concept. We have no customers, payments,
retention data, pilots, or close comparable businesses. What is its probability
of becoming a sustainable company?”

Expected behaviour:

- Define a concrete success event and time horizon before estimating.
- Spend adequate effort identifying the closest broad reference classes and
  reasoning through demand, feasibility, unit economics, channel, capital, and
  founder-execution risks.
- Provide a numeric low/high percentage range rather than refusing, returning
  `NA`, or substituting only `low`, `uncertain`, or a scenario narrative.
- Clearly label the result as a rough subjective estimate, state confidence,
  expose the assumptions and counterarguments, and avoid optimistic bias.

