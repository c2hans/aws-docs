---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_Operation.html
---

# Operation
<a name="API_Operation"></a>

A complex type that contains information about a specified operation.

## Contents
<a name="API_Operation_Contents"></a>

 ** CreateDate **   <a name="cloudmap-Type-Operation-CreateDate"></a>
The date and time that the request was submitted, in Unix date/time format and Coordinated Universal Time (UTC). The value of `CreateDate` is accurate to milliseconds. For example, the value `1516925490.087` represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** ErrorCode **   <a name="cloudmap-Type-Operation-ErrorCode"></a>
The code associated with `ErrorMessage`. Values for `ErrorCode` include the following:
+  `ACCESS_DENIED`
+  `CANNOT_CREATE_HOSTED_ZONE`
+  `EXPIRED_TOKEN`
+  `HOSTED_ZONE_NOT_FOUND`
+  `INTERNAL_FAILURE`
+  `INVALID_CHANGE_BATCH`
+  `THROTTLED_REQUEST`
Type: String
Required: No

 ** ErrorMessage **   <a name="cloudmap-Type-Operation-ErrorMessage"></a>
If the value of `Status` is `FAIL`, the reason that the operation failed.
Type: String
Required: No

 ** Id **   <a name="cloudmap-Type-Operation-Id"></a>
The ID of the operation that you want to get information about.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** OwnerAccount **   <a name="cloudmap-Type-Operation-OwnerAccount"></a>
The ID of the AWS account that owns the namespace associated with the operation.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** Status **   <a name="cloudmap-Type-Operation-Status"></a>
The status of the operation. Values include the following:
SUBMITTED
This is the initial state that occurs immediately after you submit a request.
PENDING
 AWS Cloud Map is performing the operation.
SUCCESS
The operation succeeded.
FAIL
The operation failed. For the failure reason, see `ErrorMessage`.
Type: String
Valid Values: `SUBMITTED | PENDING | SUCCESS | FAIL`
Required: No

 ** Targets **   <a name="cloudmap-Type-Operation-Targets"></a>
The name of the target entity that's associated with the operation:
NAMESPACE
The namespace ID is returned in the `ResourceId` property.
SERVICE
The service ID is returned in the `ResourceId` property.
INSTANCE
The instance ID is returned in the `ResourceId` property.
Type: String to string map
Valid Keys: `NAMESPACE | SERVICE | INSTANCE`
Value Length Constraints: Maximum length of 64.
Required: No

 ** Type **   <a name="cloudmap-Type-Operation-Type"></a>
The name of the operation that's associated with the specified ID.
Type: String
Valid Values: `CREATE_NAMESPACE | DELETE_NAMESPACE | UPDATE_NAMESPACE | UPDATE_SERVICE | REGISTER_INSTANCE | DEREGISTER_INSTANCE`
Required: No

 ** UpdateDate **   <a name="cloudmap-Type-Operation-UpdateDate"></a>
The date and time that the value of `Status` changed to the current value, in Unix date/time format and Coordinated Universal Time (UTC). The value of `UpdateDate` is accurate to milliseconds. For example, the value `1516925490.087` represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

## See Also
<a name="API_Operation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/Operation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/Operation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/Operation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
