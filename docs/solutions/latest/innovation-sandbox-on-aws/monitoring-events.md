---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/monitoring-events.html
---

# Events
<a name="monitoring-events"></a>

Innovation Sandbox publishes domain events to a dedicated Amazon EventBridge event bus (`<namespace>-ISBEventBus`). You can use these events for audit trails, custom automation, or integration with external systems.

## Consuming events
<a name="consuming-events"></a>

To consume events from the ISB event bus, create an Amazon EventBridge rule that matches the event patterns you are interested in. Common targets include:
+ An Amazon SNS topic for notifications
+ An AWS Lambda function for custom automation
+ An Amazon SQS queue for reliable downstream processing
+ Amazon CloudWatch Logs for audit archival

## Event structure
<a name="event-structure"></a>

All Innovation Sandbox events follow this standard EventBridge structure:

```
{
  "version": "0",
  "id": "event-id",
  "detail-type": "EventDetailType",
  "source": "innovation-sandbox",
  "account": "123456789012",
  "time": "2024-01-15T14:30:25Z",
  "region": "us-east-1",
  "detail": {
    // Event-specific payload (documented below)
  }
}
```

## Event categories
<a name="event-categories"></a>

Events are organized into the following categories:
+  **Lease Lifecycle Events** - Lease creation, approval, denial, and termination
+  **Lease Monitoring Events** - Budget and duration threshold alerts
+  **Lease Assignment Events** - Requests to share a lease, and confirmed access grants and removals
+  **Account Management Events** - Account cleanup, drift detection, and account quarantine (automatic and manual)
+  **Cost Reporting Events** - Cost report generation and failures
+  **Blueprint Deployment Events** - Blueprint deployment requests, successes, and failures

## Lease lifecycle events
<a name="lease-lifecycle-events"></a>

### LeaseRequested
<a name="lease-requested"></a>

Published when a user submits a new lease request.

 **Detail Type:** `LeaseRequested`

 **Schema:**

```
{
  "detail-type": "LeaseRequested",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "comments": "Need AWS environment for ML experimentation",
    "userEmail": "developer@example.com",
    "requiresManualApproval": true
  }
}
```

### LeaseApproved
<a name="lease-approved"></a>

Published when a lease request is approved and the user gains access to their sandbox account.

 **Detail Type:** `LeaseApproved`

 **Schema:**

```
{
  "detail-type": "LeaseApproved",
  "detail": {
    "leaseId": "550e8400-e29b-41d4-a716-446655440000",
    "approvedBy": "manager@example.com",
    "userEmail": "developer@example.com"
  }
}
```

### LeaseDenied
<a name="lease-denied"></a>

Published when a lease request is denied by an approver.

 **Detail Type:** `LeaseDenied`

 **Schema:**

```
{
  "detail-type": "LeaseDenied",
  "detail": {
    "leaseId": "550e8400-e29b-41d4-a716-446655440000",
    "deniedBy": "manager@example.com",
    "userEmail": "developer@example.com"
  }
}
```

### LeaseTerminated
<a name="lease-terminated"></a>

Published when a lease is terminated for any reason. The reason field provides specific details about why the lease was terminated.

 **Detail Type:** `LeaseTerminated`

 **Schema:**

```
{
  "detail-type": "LeaseTerminated",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "reason": {
      "type": "BudgetExceeded",
      "budget": 100.00,
      "totalSpend": 105.50
    }
  }
}
```

 **Reason Types:** `Expired`, `BudgetExceeded`, `ManuallyTerminated`, `UserTerminated`, `AccountQuarantined`, `Ejected`, `ProvisioningFailed`

 `UserTerminated` indicates that the leaseholder terminated their own lease; `ManuallyTerminated` indicates termination by an administrator or manager.

## Lease monitoring events
<a name="lease-monitoring-events"></a>

### LeaseBudgetThresholdAlert
<a name="lease-budget-threshold-alert"></a>

Published when a lease’s spending reaches a configured budget threshold percentage.

 **Detail Type:** `LeaseBudgetThresholdAlert`

 **Schema:**

```
{
  "detail-type": "LeaseBudgetThresholdAlert",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "budget": 100.00,
    "totalSpend": 80.00,
    "budgetThresholdTriggered": 0.8,
    "actionRequested": "ALERT"
  }
}
```

### LeaseBudgetExceeded
<a name="lease-budget-exceeded"></a>

Published when a lease’s spending exceeds the configured budget limit.

 **Detail Type:** `LeaseBudgetExceeded`

 **Schema:**

```
{
  "detail-type": "LeaseBudgetExceeded",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "budget": 100.00,
    "totalSpend": 105.50
  }
}
```

### LeaseDurationThresholdAlert
<a name="lease-duration-threshold-alert"></a>

Published when a lease reaches a configured duration threshold.

 **Detail Type:** `LeaseDurationThresholdAlert`

 **Schema:**

```
{
  "detail-type": "LeaseDurationThresholdAlert",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "triggeredDurationThreshold": 24,
    "leaseDurationInHours": 168,
    "actionRequested": "ALERT"
  }
}
```

### LeaseFreezingThresholdAlert
<a name="lease-freezing-threshold-alert"></a>

Published when a lease reaches a threshold that triggers a freezing action. This event uses the same schema as LeaseFrozen.

 **Detail Type:** `LeaseFreezingThresholdAlert`

 **Schema:**

```
{
  "detail-type": "LeaseFreezingThresholdAlert",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "reason": {
      "type": "BudgetExceeded",
      "triggeredBudgetThreshold": 0.95,
      "budget": 100.00,
      "totalSpend": 95.00
    }
  }
}
```

### LeaseExpired
<a name="lease-expired"></a>

Published when a lease expires due to reaching its maximum duration.

 **Detail Type:** `LeaseExpired`

 **Schema:**

```
{
  "detail-type": "LeaseExpired",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "leaseExpirationDate": "2024-01-22T14:30:25Z"
  }
}
```

### LeaseFrozen
<a name="lease-frozen"></a>

Published when a lease is frozen (access suspended but not terminated).

 **Detail Type:** `LeaseFrozen`

 **Schema:**

```
{
  "detail-type": "LeaseFrozen",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "reason": {
      "type": "BudgetExceeded",
      "triggeredBudgetThreshold": 0.95,
      "budget": 100.00,
      "totalSpend": 95.00
    }
  }
}
```

### LeaseUnfrozen
<a name="lease-unfrozen"></a>

Published when a previously frozen lease is unfrozen and access is restored.

 **Detail Type:** `LeaseUnfrozen`

 **Schema:**

```
{
  "detail-type": "LeaseUnfrozen",
  "detail": {
    "leaseId": {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "accountId": "123456789012",
    "maxBudget": 100.00,
    "leaseDurationInHours": 168,
    "reason": "Budget threshold resolved, access restored"
  }
}
```

## Lease assignment events
<a name="lease-assignment-events"></a>

These events support the lease sharing feature. The solution records the desired set of users and groups for a lease, then processes IAM Identity Center access grants and removals asynchronously through an AWS Step Functions workflow. For more information on the sharing feature, refer to [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing) in the Manager Guide.

The solution publishes `AssignmentCreated` and `AssignmentRemoved` events only for confirmed access changes. A principal that was already assigned and remains assigned produces no event, so the number of these events for a given request does not necessarily match the number of principals on the lease.

### AssignmentRequested
<a name="assignment-requested"></a>

Published when the desired assignments for a lease change (for example, when a user is added or removed, or during lease publish, freeze, unfreeze, or termination). This event triggers the assignment processing AWS Step Functions workflow.

 **Detail Type:** `AssignmentRequested`

 **Schema:**

```
{
  "detail-type": "AssignmentRequested",
  "detail": {
    "intent": "UPDATE",
    "leaseId": "550e8400-e29b-41d4-a716-446655440000",
    "requestedBy": "manager@example.com",
    "lockOwnerId": "update-550e8400-e29b-41d4-a716-446655440000",
    "leaseOwnerEmail": "developer@example.com"
  }
}
```

 **Intent values:** `UPDATE`, `PUBLISH`, `FREEZE`, `UNFREEZE`, `TERMINATE`

The `lockOwnerId` is a lock ownership token, formatted as the lowercased intent followed by a UUID. The solution generates this token when it acquires the lease’s resource lock, and the assignment processing AWS Step Functions workflow uses it to verify it still owns that lock before releasing it.

### AssignmentCreated
<a name="assignment-created"></a>

Published when a principal (user or group) is successfully granted access to a sandbox account. This event triggers an email notification to the lease owner and, for user assignments, to the added user.

 **Detail Type:** `AssignmentCreated`

 **Schema:**

```
{
  "detail-type": "AssignmentCreated",
  "detail": {
    "leaseId": "550e8400-e29b-41d4-a716-446655440000",
    "principalId": "94482488-3041-7098-1234-abcdef123456",
    "principalType": "USER",
    "assigneeEmail": "teammate@example.com",
    "accountId": "123456789012",
    "addedBy": "developer@example.com",
    "leaseOwner": "developer@example.com"
  }
}
```

 **Note:** `assigneeEmail` is present for `USER` assignments and absent for `GROUP` assignments.

### AssignmentRemoved
<a name="assignment-removed"></a>

Published when a principal’s access to a sandbox account is successfully removed (for example, when a user is removed from the assignments, or during lease freeze or termination). This event triggers an email notification to the lease owner.

 **Detail Type:** `AssignmentRemoved`

 **Schema:**

```
{
  "detail-type": "AssignmentRemoved",
  "detail": {
    "leaseId": "550e8400-e29b-41d4-a716-446655440000",
    "principalId": "94482488-3041-7098-1234-abcdef123456",
    "principalType": "USER",
    "assigneeEmail": "teammate@example.com",
    "accountId": "123456789012",
    "removedBy": "developer@example.com",
    "leaseOwner": "developer@example.com"
  }
}
```

 **Note:** `assigneeEmail` is present for `USER` assignments and absent for `GROUP` assignments.

## Account management events
<a name="account-management-events"></a>

### CleanAccountRequest
<a name="clean-account-request"></a>

Published when an account cleanup process is initiated.

 **Detail Type:** `CleanAccountRequest`

 **Schema:**

```
{
  "detail-type": "CleanAccountRequest",
  "detail": {
    "accountId": "123456789012",
    "reason": "Lease terminated - budget exceeded"
  }
}
```

### AccountCleanupSucceeded
<a name="account-cleanup-succeeded"></a>

Published when an account cleanup process completes successfully.

 **Detail Type:** `AccountCleanupSucceeded`

 **Schema:**

```
{
  "detail-type": "AccountCleanupSucceeded",
  "detail": {
    "accountId": "123456789012",
    "reason": "LEASE_TERMINATION",
    "cleanupExecutionContext": {
      "executionArn": "arn:aws:lambda:us-east-1:123456789012:function:isb-durable-cleanup:live:execution-id",
      "executionStartTime": "2024-01-15T14:30:25Z"
    }
  }
}
```

### AccountCleanupFailed
<a name="account-cleanup-failed"></a>

Published when an account cleanup process fails.

 **Detail Type:** `AccountCleanupFailed`

 **Schema:**

```
{
  "detail-type": "AccountCleanupFailed",
  "detail": {
    "accountId": "123456789012",
    "reason": "LEASE_TERMINATION",
    "cleanupExecutionContext": {
      "executionArn": "arn:aws:lambda:us-east-1:123456789012:function:isb-durable-cleanup:live:execution-id",
      "executionStartTime": "2024-01-15T14:30:25Z"
    }
  }
}
```

### AccountQuarantined
<a name="account-quarantined"></a>

Published when an account is quarantined because of cleanup failures, detected drift, or manual quarantine by an administrator.

 **Detail Type:** `AccountQuarantined`

 **Schema:**

```
{
  "detail-type": "AccountQuarantined",
  "detail": {
    "awsAccountId": "123456789012",
    "reason": "Account cleanup failed after multiple attempts"
  }
}
```

### AccountDriftDetected
<a name="account-drift-detected"></a>

Published when an account is detected to be in an unexpected organizational unit.

 **Detail Type:** `AccountDriftDetected`

 **Schema:**

```
{
  "detail-type": "AccountDriftDetected",
  "detail": {
    "accountId": "123456789012",
    "actualOu": "ou-root-1234567890",
    "expectedOu": "ou-sandbox-0987654321"
  }
}
```

## Cost reporting events
<a name="cost-reporting-events"></a>

### GroupCostReportGenerated
<a name="group-cost-report-generated"></a>

Published when a cost report is successfully generated for a group of accounts.

 **Detail Type:** `GroupCostReportGenerated`

 **Schema:**

```
{
  "detail-type": "GroupCostReportGenerated",
  "detail": {
    "reportMonth": "2024-01",
    "fileName": "cost-report-2024-01.csv",
    "bucketName": "innovation-sandbox-reports-bucket",
    "timestamp": "2024-02-01T09:00:00Z"
  }
}
```

### GroupCostReportGeneratedFailure
<a name="group-cost-report-generated-failure"></a>

Published when cost report generation fails.

 **Detail Type:** `GroupCostReportGeneratedFailure`

 **Schema:**

```
{
  "detail-type": "GroupCostReportGeneratedFailure",
  "detail": {
    "reportMonth": "2024-01",
    "timestamp": "2024-02-01T09:00:00Z"
  }
}
```

## Blueprint deployment events
<a name="blueprint-deployment-events"></a>

### BlueprintDeploymentRequest
<a name="blueprint-deployment-request"></a>

Published when a lease with an attached blueprint is approved, triggering the blueprint deployment workflow.

 **Detail Type:** `BlueprintDeploymentRequest`

 **Schema:**

```
{
  "detail-type": "BlueprintDeploymentRequest",
  "detail": {
    "blueprintId": "550e8400-e29b-41d4-a716-446655440000",
    "blueprintName": "Development Environment",
    "leaseId": "650e8400-e29b-41d4-a716-446655440000",
    "userEmail": "developer@example.com",
    "accountId": "123456789012",
    "stackSetId": "arn:aws:cloudformation:us-east-1:123456789012:stackset/dev-env-stackset:abc123",
    "regions": ["us-east-1", "us-west-2"],
    "regionConcurrencyType": "SEQUENTIAL",
    "deploymentTimeoutMinutes": 30,
    "maxConcurrentPercentage": 100,
    "failureTolerancePercentage": 0,
    "concurrencyMode": "STRICT_FAILURE_TOLERANCE"
  }
}
```

 **Note:** `maxConcurrentPercentage`, `failureTolerancePercentage`, and `concurrencyMode` are optional fields.

### BlueprintDeploymentSucceeded
<a name="blueprint-deployment-succeeded"></a>

Published when a blueprint deployment completes successfully and the user can access the account with pre-configured resources.

 **Detail Type:** `BlueprintDeploymentSucceeded`

 **Schema:**

```
{
  "detail-type": "BlueprintDeploymentSucceeded",
  "detail": {
    "leaseId": {
      "uuid": "650e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "blueprintId": "550e8400-e29b-41d4-a716-446655440000",
    "accountId": "123456789012",
    "operationId": "abc123-def456-ghi789",
    "duration": 15
  }
}
```

### BlueprintDeploymentFailed
<a name="blueprint-deployment-failed"></a>

Published when a blueprint deployment fails due to validation errors, deployment failures, or timeouts. The lease transitions to `ProvisioningFailed` status and the account is sent to cleanup.

 **Detail Type:** `BlueprintDeploymentFailed`

 **Schema:**

```
{
  "detail-type": "BlueprintDeploymentFailed",
  "detail": {
    "leaseId": {
      "uuid": "650e8400-e29b-41d4-a716-446655440000",
      "userEmail": "developer@example.com"
    },
    "blueprintId": "550e8400-e29b-41d4-a716-446655440000",
    "accountId": "123456789012",
    "operationId": "abc123-def456-ghi789",
    "errorType": "DEPLOYMENT_TIMEOUT",
    "errorMessage": "StackSet deployment failed: Resource creation timeout"
  }
}
```

 **Note:** `operationId` is optional and may not be present for validation failures that occur before deployment starts.

 **Common failure reasons:**
+ StackSet validation failures (not found, wrong permission model, inactive status)
+ CloudFormation deployment errors (resource creation failures, insufficient permissions)
+ Deployment timeout exceeded (default: 30 minutes, configurable per blueprint)
+ Lambda function errors (crashes, timeouts, throttling)

## Schema evolution
<a name="schema-evolution"></a>

Event schemas may evolve over time. Design your integration to be resilient:
+ Ignore unknown fields in event payloads
+ Provide default values for missing optional fields
+ Version your event processing logic when breaking changes occur

For the complete source code, refer to the Innovation Sandbox on AWS [GitHub repository](https://github.com/aws-solutions/innovation-sandbox-on-aws).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
