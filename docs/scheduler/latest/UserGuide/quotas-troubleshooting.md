---
source_url: https://docs.aws.amazon.com/scheduler/latest/UserGuide/quotas-troubleshooting.html
---

# Troubleshooting quotas in EventBridge Scheduler
<a name="quotas-troubleshooting"></a>

Use the following information to help you diagnose and fix common issues that you might encounter concerning EventBridge Scheduler quotas.

## ServiceQuotaExceededException
<a name="troubleshooting_error_code_1"></a>

I am receiving throttling errors on `CreateSchedule`, `DeleteSchedule`, `GetSchedule`, or `UpdateSchedule` request rate, even though I am below the default rate limit.

### Common cause
<a name="troubleshooting_common_cause"></a>

On September 7, 2023, EventBridge Scheduler began supporting the ScheduleGroup ARN (Amazon Resource Name) instead of the Schedule ARN in execution role trust policies. Customers allowlisted to continue using Schedule ARNs in their trust policy may have limits of 50 TPS, instead of the default limits of 250 to 1000 TPS (dependent on region).

### Resolution
<a name="troubleshooting_resolution"></a>

Contact [support](https://console.aws.amazon.com/support/home?#/case/create?issueType=technical) to request a higher maximum limit.

### Prevention
<a name="troubleshooting_prevention"></a>

Modify your existing trust policies in one of the following way:
+ Removing all scoping from the role.
+ Scoping the role so that it may be assumed using the Schedule ARN or the ScheduleGroup ARN.

  For example, suppose you had the following existing trust policy:

  ```
  {
      "Effect": "Allow",
      "Principal": {
          "Service": "scheduler.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
          "StringEquals": {
              "aws:SourceArn": "arn:aws:scheduler:{{region}}:{{account}}:schedule/{{schedule_group}}/{{schedule}}"
          }
      }
  }
  ```

  You could update the trust policy to the following:

  ```
  {
      "Effect": "Allow",
      "Principal": {
          "Service": "scheduler.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
          "ForAnyValue:StringEquals": {
              "aws:SourceArn": [
                  "arn:aws:scheduler:{{region}}:{{account}}:schedule/{{schedule_group}}/{{schedule}}",
                  "arn:aws:scheduler:{{region}}:{{account}}:schedule-group/{{schedule_group}}"
              ]
          }
      }
  }
  ```
