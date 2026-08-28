---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html
---

# CreateDomain
<a name="API_connect-customer-profiles_CreateDomain"></a>

Creates a domain, which is a container for all customer data, such as customer profile attributes, object types, profile keys, and encryption keys. You can create multiple domains, and each domain can have multiple third-party integrations.

Each Connect Customer instance can be associated with only one domain. Multiple Connect Customer instances can be associated with one domain.

Use this API or [UpdateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html) to enable [identity resolution](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html): set `Matching` to true.

To prevent cross-service impersonation when you call this API, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html) for sample policies that you should apply.

**Note**
It is not possible to associate a Customer Profiles domain with an Amazon Connect Instance directly from the API. If you would like to create a domain and associate a Customer Profiles domain, use the Amazon Connect admin website. For more information, see [Enable Customer Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/enable-customer-profiles.html#enable-customer-profiles-step1).
Each Amazon Connect instance can be associated with only one domain. Multiple Amazon Connect instances can be associated with one domain.

## Request Syntax
<a name="API_connect-customer-profiles_CreateDomain_RequestSyntax"></a>

```
POST /domains/{{DomainName}} HTTP/1.1
Content-type: application/json

{
   "DataStore": {
      "Enabled": {{boolean}}
   },
   "DeadLetterQueueUrl": "{{string}}",
   "DefaultEncryptionKey": "{{string}}",
   "DefaultExpirationDays": {{number}},
   "Matching": {
      "AutoMerging": {
         "ConflictResolution": {
            "ConflictResolvingModel": "{{string}}",
            "SourceName": "{{string}}"
         },
         "Consolidation": {
            "MatchingAttributesList": [
               [ "{{string}}" ]
            ]
         },
         "Enabled": {{boolean}},
         "MinAllowedConfidenceScoreForMerging": {{number}}
      },
      "Enabled": {{boolean}},
      "ExportingConfig": {
         "S3Exporting": {
            "S3BucketName": "{{string}}",
            "S3KeyName": "{{string}}"
         }
      },
      "JobSchedule": {
         "DayOfTheWeek": "{{string}}",
         "Time": "{{string}}"
      }
   },
   "RuleBasedMatching": {
      "AttributeTypesSelector": {
         "Address": [ "{{string}}" ],
         "AttributeMatchingModel": "{{string}}",
         "EmailAddress": [ "{{string}}" ],
         "PhoneNumber": [ "{{string}}" ]
      },
      "ConflictResolution": {
         "ConflictResolvingModel": "{{string}}",
         "SourceName": "{{string}}"
      },
      "Enabled": {{boolean}},
      "ExportingConfig": {
         "S3Exporting": {
            "S3BucketName": "{{string}}",
            "S3KeyName": "{{string}}"
         }
      },
      "MatchingRules": [
         {
            "Rule": [ "{{string}}" ]
         }
      ],
      "MaxAllowedRuleLevelForMatching": {{number}},
      "MaxAllowedRuleLevelForMerging": {{number}}
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataStore](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-DataStore"></a>
Set to true to enabled data store for this domain.
Type: [DataStoreRequest](API_connect-customer-profiles_DataStoreRequest.md) object
Required: No

 ** [DeadLetterQueueUrl](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-DeadLetterQueueUrl"></a>
The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [DefaultEncryptionKey](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-DefaultEncryptionKey"></a>
The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [DefaultExpirationDays](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-DefaultExpirationDays"></a>
The default number of days until the data within the domain expires.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.
Required: Yes

 ** [Matching](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-Matching"></a>
The process of matching duplicate profiles. If `Matching` = `true`, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains.
After the Identity Resolution Job completes, use the [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) API to return and review the results. Or, if you have configured `ExportingConfig` in the `MatchingRequest`, you can download the results from S3.
Type: [MatchingRequest](API_connect-customer-profiles_MatchingRequest.md) object
Required: No

 ** [RuleBasedMatching](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-RuleBasedMatching"></a>
The process of matching duplicate profiles using the Rule-Based matching. If `RuleBasedMatching` = true, Connect Customer Customer Profiles will start to match and merge your profiles according to your configuration in the `RuleBasedMatchingRequest`. You can use the `ListRuleBasedMatches` and `GetSimilarProfiles` API to return and review the results. Also, if you have configured `ExportingConfig` in the `RuleBasedMatchingRequest`, you can download the results from S3.
Type: [RuleBasedMatchingRequest](API_connect-customer-profiles_RuleBasedMatchingRequest.md) object
Required: No

 ** [Tags](#API_connect-customer-profiles_CreateDomain_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "DataStore": {
      "Enabled": boolean,
      "Readiness": {
         "Message": "string",
         "ProgressPercentage": number
      }
   },
   "DeadLetterQueueUrl": "string",
   "DefaultEncryptionKey": "string",
   "DefaultExpirationDays": number,
   "DomainName": "string",
   "LastUpdatedAt": number,
   "Matching": {
      "AutoMerging": {
         "ConflictResolution": {
            "ConflictResolvingModel": "string",
            "SourceName": "string"
         },
         "Consolidation": {
            "MatchingAttributesList": [
               [ "string" ]
            ]
         },
         "Enabled": boolean,
         "MinAllowedConfidenceScoreForMerging": number
      },
      "Enabled": boolean,
      "ExportingConfig": {
         "S3Exporting": {
            "S3BucketName": "string",
            "S3KeyName": "string"
         }
      },
      "JobSchedule": {
         "DayOfTheWeek": "string",
         "Time": "string"
      }
   },
   "RuleBasedMatching": {
      "AttributeTypesSelector": {
         "Address": [ "string" ],
         "AttributeMatchingModel": "string",
         "EmailAddress": [ "string" ],
         "PhoneNumber": [ "string" ]
      },
      "ConflictResolution": {
         "ConflictResolvingModel": "string",
         "SourceName": "string"
      },
      "Enabled": boolean,
      "ExportingConfig": {
         "S3Exporting": {
            "S3BucketName": "string",
            "S3KeyName": "string"
         }
      },
      "MatchingRules": [
         {
            "Rule": [ "string" ]
         }
      ],
      "MaxAllowedRuleLevelForMatching": number,
      "MaxAllowedRuleLevelForMerging": number,
      "Status": "string"
   },
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp

 ** [DataStore](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-DataStore"></a>
The data store.
Type: [DataStoreResponse](API_connect-customer-profiles_DataStoreResponse.md) object

 ** [DeadLetterQueueUrl](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-DeadLetterQueueUrl"></a>
The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [DefaultEncryptionKey](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-DefaultEncryptionKey"></a>
The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [DefaultExpirationDays](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-DefaultExpirationDays"></a>
The default number of days until the data within the domain expires.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.

 ** [DomainName](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-LastUpdatedAt"></a>
The timestamp of when the domain was most recently edited.
Type: Timestamp

 ** [Matching](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-Matching"></a>
The process of matching duplicate profiles. If `Matching` = `true`, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains.
After the Identity Resolution Job completes, use the [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) API to return and review the results. Or, if you have configured `ExportingConfig` in the `MatchingRequest`, you can download the results from S3.
Type: [MatchingResponse](API_connect-customer-profiles_MatchingResponse.md) object

 ** [RuleBasedMatching](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-RuleBasedMatching"></a>
The process of matching duplicate profiles using the Rule-Based matching. If `RuleBasedMatching` = true, Connect Customer Customer Profiles will start to match and merge your profiles according to your configuration in the `RuleBasedMatchingRequest`. You can use the `ListRuleBasedMatches` and `GetSimilarProfiles` API to return and review the results. Also, if you have configured `ExportingConfig` in the `RuleBasedMatchingRequest`, you can download the results from S3.
Type: [RuleBasedMatchingResponse](API_connect-customer-profiles_RuleBasedMatchingResponse.md) object

 ** [Tags](#API_connect-customer-profiles_CreateDomain_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomain-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_CreateDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## Examples
<a name="API_connect-customer-profiles_CreateDomain_Examples"></a>

### Example
<a name="API_connect-customer-profiles_CreateDomain_Example_1"></a>

This example illustrates one usage of CreateDomain.

#### Sample Request
<a name="API_connect-customer-profiles_CreateDomain_Example_1_Request"></a>

```
POST /v1/domains/ExampleDomainName
Content-type: application/json
{
   "DeadLetterQueueUrl": "arn:aws:sqs:us-east-1:123456789012:DLQName",
   "DefaultEncryptionKey": "arn:aws:kms:us-east-1:123456789012:key/1988472d-6b77-4bb6-ae39-efce5EXAMPLE",
   "DefaultExpirationDays": 1098,
   "DomainName":"ExampleDomainName"
}
```

#### Sample Response
<a name="API_connect-customer-profiles_CreateDomain_Example_1_Response"></a>

```
Content-type: application/json
{
   "DeadLetterQueueUrl": "arn:aws:sqs:us-east-1:123456789012:DLQName",
   "CreatedAt": 1479249799770,
   "DefaultEncryptionKey":"arn:aws:kms:us-east-1:123456789012:key/1988472d-6b77-4bb6-ae39-efce5EXAMPLE",
   "DefaultExpirationDays": 1098,
   "LastUpdatedAt":1479249799770,
   "DomainName": "ExampleDomainName"
}
```

## See Also
<a name="API_connect-customer-profiles_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
