---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ChangeEvent.html
---

# ChangeEvent
<a name="API_ChangeEvent"></a>

A structure that contains information about a change event that occurred for a service, such as a deployment or configuration change.

## Contents
<a name="API_ChangeEvent_Contents"></a>

 ** AccountId **   <a name="applicationsignals-Type-ChangeEvent-AccountId"></a>
The AWS account ID where this change event occurred.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** ChangeEventType **   <a name="applicationsignals-Type-ChangeEvent-ChangeEventType"></a>
The type of change event that occurred, such as `DEPLOYMENT`.
Type: String
Valid Values: `DEPLOYMENT | CONFIGURATION`
Required: Yes

 ** Entity **   <a name="applicationsignals-Type-ChangeEvent-Entity"></a>
The entity (service or resource) that was affected by this change event, including its key attributes.
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this is.
+  `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+  `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Environment` specifies the location where this object is hosted, or what it belongs to.
+  `AwsAccountId` specifies the account where this object is in.
Below is an example of a service.
 `{ "Type": "Service", "Name": "visits-service", "Environment": "petclinic-test" }`
Below is an example of a resource.
 `{ "Type": "AWS::Resource", "ResourceType": "AWS::DynamoDB::Table", "Identifier": "Customers" }`
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** EventId **   <a name="applicationsignals-Type-ChangeEvent-EventId"></a>
A unique identifier for this change event. For CloudTrail-based events, this is the CloudTrail event id. For other events, this will be `Unknown`.
Type: String
Required: Yes

 ** Region **   <a name="applicationsignals-Type-ChangeEvent-Region"></a>
The AWS region where this change event occurred.
Type: String
Required: Yes

 ** Timestamp **   <a name="applicationsignals-Type-ChangeEvent-Timestamp"></a>
The timestamp when this change event occurred. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.
Type: Timestamp
Required: Yes

 ** EventName **   <a name="applicationsignals-Type-ChangeEvent-EventName"></a>
The name or description of this change event.
Type: String
Required: No

 ** UserName **   <a name="applicationsignals-Type-ChangeEvent-UserName"></a>
The name of the user who initiated this change event, if available.
Type: String
Required: No

## See Also
<a name="API_ChangeEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ChangeEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ChangeEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ChangeEvent)
