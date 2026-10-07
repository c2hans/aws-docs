---
name: deadline-cloud-test-methods
description: Deadline Cloud (container data-sharing) live-test facts — CMF credential-vending oracle, SMF-only remanence gating, AWS-authored IAM artifacts
metadata:
  type: reference
---

Deadline Cloud container-data-sharing plan, Sweep-3, run 20261006-deadline (both accounts [[agentcore-env]]). boto3 service `deadline`, us-east-1, 126 ops. No `CreateVolume` (service-created only).

**Cheap live substrate — Customer-Managed Fleet (CMF) launches NO EC2, runs NO job code.** Lets you exercise the full control-plane credential-vending path without touching an SMF/managed host (the hard-stop surface). Standup order:
1. IAM roles first: fleet role must trust BOTH `deadline.amazonaws.com` AND `credentials.deadline.amazonaws.com` (CreateFleet validates sts:AssumeRole by credentials.deadline...). Queue roles trust `credentials.deadline.amazonaws.com`. All with `aws:SourceAccount`.
2. CreateFarm (no kmsKeyArn = service-owned key). CreateFleet configuration.customerManaged{mode:NO_SCALING, workerCapabilities{vCpuCount.min, memoryMiB.min, osFamily:LINUX, cpuArchitectureType:x86_64}}, roleArn=fleet role, maxWorkerCount>=1.
3. CreateQueue needs roleArn; **must UpdateQueue jobRunAsUser{runAs:WORKER_AGENT_USER}** before CreateQueueFleetAssociation (else "Unable to determine jobRunAsUser").
4. CreateWorker(farmId,fleetId) -> worker in CREATED. Drive to STARTED via UpdateWorker(status=STARTED, capabilities={amounts:[amount.worker.vcpu,amount.worker.memory], attributes:[attr.worker.os.family=[linux],attr.worker.cpu.arch=[x86_64]]}).
5. To make worker "working on" a queue: CreateJob(trivial OpenJD `{"specificationVersion":"jobtemplate-2023-09","name":..,"steps":[{"name":"S","script":{"actions":{"onRun":{"command":"/usr/bin/true"}}}}]}`, templateType JSON, priority 50) then poll UpdateWorkerSchedule(updatedSessionActions={}) — assignedSessions appears in ~1 poll. The job command is NEVER executed (CMF has no host) — stays control-plane.

**Teardown order (all async-ish, poll):** delete queue-env -> UpdateJob targetTaskRunStatus=CANCELED -> UpdateWorker STOPPED + DeleteWorker -> UpdateQueueFleetAssociation status=STOP_SCHEDULING_AND_CANCEL_TASKS, poll GetQueueFleetAssociation to STOPPED, DeleteQueueFleetAssociation -> DeleteQueue x2 -> DeleteFleet -> DeleteFarm -> detach/delete IAM roles. Verify list_farms=[] + get_farm->ResourceNotFoundException.

**AssumeQueueRoleForWorker credential-vending oracle (Area-6, CONFIRMED service-enforced / scope-break REFUTED):**
AWS-managed `AWSDeadlineCloud-FleetWorker` grants AssumeQueueRoleForWorker on `Resource:"*"` with ONLY `aws:PrincipalAccount==aws:ResourceAccount` — no membership/ARN scoping in IAM. BUT the SERVICE binds the vend to an **active per-queue session assignment** (tighter than fleet association):
- worker not STARTED -> ConflictException 409 "Status CREATED does not permit".
- worker STARTED, no session -> ConflictException 409 "Worker is not working on queue qX" (identical for associated AND non-associated queue).
- worker assigned a session on qA -> AssumeQueueRoleForWorker(qA)=SUCCESS; (qB not working-on)=same 409 denial; bogus queue=ResourceNotFoundException 404 (distinct, no existence-collapse).
Identical under scoped principal carrying only FleetWorker policy. So Resource:* IAM breadth is fully compensated at the service layer. Vended creds = exactly the queue's configured role, same account.

**AWS-authored IAM artifacts (clean, refute over-broad claims):**
- Generated queue-role S3 policy (docs userguide/security-iam-service-roles.md) is prefix-scoped `s3:::BUCKET/PREFIX/*` + `aws:ResourceAccount` pin; third-party-software Resource:* gated to `s3:DataAccessPointArn accesspoint/deadline-software-*` + VPC origin. Fleet-role trust sample ships `aws:SourceAccount`+`aws:SourceArn=farm/{id}` confused-deputy protection.
- `AWSDeadlineCloud-UserAccess{Queues,Fleets}`: every data action gated by `deadline:*MembershipLevels` tiers; ListJobs/ListQueues gated by `deadline:RequesterPrincipalId=${deadline:PrincipalId}`.
- Service defines resource types (farm/fleet/queue/job/volume/worker/budget/monitor/license-endpoint) + condition keys (*MembershipLevels, CalledAction, PrincipalId, RequesterPrincipalId, AssociatedMembershipLevel). NOT wildcard-only.

**EXEC-GATED / blocked (do NOT run job code on SMF — hard stop):** persistentVolumeConfiguration is SMF-only (absent from customerManaged); list_volumes on a CMF fleet = []. Cross-queue/cross-user persistent-volume & session-dir remanence (Areas 1/2/9) need SMF fleet + launched EC2 workers + persistent storage + >=2 queues + running job code = cost + hard-stop. Confirm mechanism from docs only, route exec to human.
- `AmazonEC2ContainerRegistryReadOnly` on queue/fleet role is Resource:* with no condition — but that is gate-2 disqualified ("only Resource:* too wide" on an AWS convenience managed policy = NOT a bug).
- Queue-environment template content is a customer-authored OpenJD script; CreateQueueEnvironment accepts arbitrary privileged/socket-mount scripts with NO server-side validation — but it's the author's own fleet (footgun; cross-queue impact on a shared fleet is exec-gated). FleetSoftwareAddOn.name enum = ['docker'] only.
