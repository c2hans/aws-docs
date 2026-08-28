---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplicationStatusCheckResponseObject.html
---

# ApplicationStatusCheckResponseObject
<a name="API_ApplicationStatusCheckResponseObject"></a>

Describes an application status check.

## Contents
<a name="API_ApplicationStatusCheckResponseObject_Contents"></a>

 ** aggregation **
The aggregation setting for the application status check. When set to `included`, the result of this check contributes to the instance-level application status. When set to `excluded`, the check runs independently and does not affect the instance-level status.
Type: String
Valid Values: `included | excluded`
Required: No

 ** applicationStatusCheckId **
The ID of the application status check.
Type: String
Required: No

 ** creationTime **
The date and time when the application status check was created.
Type: Timestamp
Required: No

 ** deletionTime **
The date and time when the application status check was deleted.
Type: Timestamp
Required: No

 ** deviceIndex **
The index of the network device used for the health check. The value is greater than or equal to 0.
Type: Integer
Required: No

 ** failureThreshold **
The number of consecutive failed health checks before the application status is considered impaired. The value must be greater than 0.
Type: Integer
Required: No

 ** HealthCheckPathSet.N **
The health check paths for the application status check.
Type: Array of [HealthCheckPathResponseObject](API_HealthCheckPathResponseObject.md) objects
Required: No

 ** initializationGracePeriodSeconds **
The number of seconds to wait before starting health checks after an instance is launched. Valid values: 1 to 600.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 600.
Required: No

 ** interval **
The interval, in seconds, between health checks. Valid value: 60.
Type: Integer
Required: No

 ** ipScope **
The IP scope used for the health check.
Type: String
Valid Values: `private`
Required: No

 ** ipVersion **
The IP version used for the health check.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** lastUpdatedAt **
The date and time when the application status check was last updated.
Type: Timestamp
Required: No

 ** modifyTime **
The date and time when the application status check was last modified.
Type: Timestamp
Required: No

 ** path **
The URL path used for the health check HTTP request.
Type: String
Required: No

 ** port **
The port used for the health check.
Type: Integer
Required: No

 ** protocol **
The protocol used for the health check.
Type: String
Valid Values: `http | https`
Required: No

 ** statusCodeMatcher **
The comma-separated list of individual HTTP status codes or ranges that indicate a successful health check response.
Type: String
Required: No

 ** successThreshold **
The number of consecutive successful health checks before the application status is considered healthy. The value must be greater than 0.
Type: Integer
Required: No

 ** TagSet.N **
The tags assigned to the application status check.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TargetTagAssociationSet.N **
The [tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) associated with the application status check. Instances with these tags are automatically monitored by this check.
Type: Array of [CustomTagKeyValueResponsePair](API_CustomTagKeyValueResponsePair.md) objects
Required: No

 ** timeout **
The amount of time, in seconds, to wait for a health check response. Valid values: 1 to 30.
Type: Integer
Required: No

## See Also
<a name="API_ApplicationStatusCheckResponseObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplicationStatusCheckResponseObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplicationStatusCheckResponseObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplicationStatusCheckResponseObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
