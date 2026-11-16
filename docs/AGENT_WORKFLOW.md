# Agent workflow and handoff

Coordinator owns architecture, contracts, milestone acceptance and merge order. Suggested roles: data/embedding agent, index/serving agent, benchmark/baseline agent, integration reviewer. Delegate only with explicit authorization or applicable instructions and assign disjoint files; avoid concurrent schema edits.

Each task records: task ID, owner, branch, input revisions, scope, dependencies, acceptance checks and artifact paths. Each handoff records: completed changes, exact test commands/results, unresolved failures, assumptions, branch/head and next executable command. Commit at milestone boundaries; open a reviewable PR with evidence and limitations; merge after checks pass under user authorization.

Resume from MEMORY.md plus repository state. A context summary is not evidence that a command succeeded. Mark tasks complete only after acceptance checks. If quota interrupts work, checkpoint what can be saved; no markdown instruction can guarantee automatic restart on quota reset.
