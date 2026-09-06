---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeDomain.html
---

# UpgradeDomain
<a name="API_UpgradeDomain"></a>

Allows you to either upgrade your Amazon OpenSearch Service domain or perform an upgrade eligibility check to a compatible version of OpenSearch or Elasticsearch.

## Request Syntax
<a name="API_UpgradeDomain_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/upgradeDomain HTTP/1.1
Content-type: application/json

{
   "AdvancedOptions": {
      "{{string}}" : "{{string}}"
   },
   "DomainName": "{{string}}",
   "PerformCheckOnly": {{boolean}},
   "TargetVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpgradeDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpgradeDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdvancedOptions](#API_UpgradeDomain_RequestSyntax) **   <a name="opensearchservice-UpgradeDomain-request-AdvancedOptions"></a>
Only supports the `override_main_response_version` parameter and not other advanced options. You can only include this option when upgrading to an OpenSearch version. Specifies whether the domain reports its version as 7.10 so that it continues to work with Elasticsearch OSS clients and plugins.
Type: String to string map
Required: No

 ** [DomainName](#API_UpgradeDomain_RequestSyntax) **   <a name="opensearchservice-UpgradeDomain-request-DomainName"></a>
Name of the OpenSearch Service domain that you want to upgrade.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [PerformCheckOnly](#API_UpgradeDomain_RequestSyntax) **   <a name="opensearchservice-UpgradeDomain-request-PerformCheckOnly"></a>
When true, indicates that an upgrade eligibility check needs to be performed. Does not actually perform the upgrade.
Type: Boolean
Required: No

 ** [TargetVersion](#API_UpgradeDomain_RequestSyntax) **   <a name="opensearchservice-UpgradeDomain-request-TargetVersion"></a>
OpenSearch or Elasticsearch version to which you want to upgrade, in the format Opensearch\_X.Y or Elasticsearch\_X.Y.
Type: String
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: Yes

## Response Syntax
<a name="API_UpgradeDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdvancedOptions": {
      "string" : "string"
   },
   "ChangeProgressDetails": {
      "ChangeId": "string",
      "ConfigChangeStatus": "string",
      "InitiatedBy": "string",
      "LastUpdatedTime": number,
      "Message": "string",
      "StartTime": number
   },
   "DomainName": "string",
   "PerformCheckOnly": boolean,
   "TargetVersion": "string",
   "UpgradeId": "string"
}
```

## Response Elements
<a name="API_UpgradeDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdvancedOptions](#API_UpgradeDomain_ResponseSyntax) **   <a name="opensearchservice-UpgradeDomain-response-AdvancedOptions"></a>
The advanced options configuration for the domain.
Type: String to string map

 ** [ChangeProgressDetails](#API_UpgradeDomain_ResponseSyntax) **   <a name="opensearchservice-UpgradeDomain-response-ChangeProgressDetails"></a>
Container for information about a configuration change happening on a domain.
Type: [ChangeProgressDetails](API_ChangeProgressDetails.md) object

 ** [DomainName](#API_UpgradeDomain_ResponseSyntax) **   <a name="opensearchservice-UpgradeDomain-response-DomainName"></a>
The name of the domain that was upgraded.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`

 ** [PerformCheckOnly](#API_UpgradeDomain_ResponseSyntax) **   <a name="opensearchservice-UpgradeDomain-response-PerformCheckOnly"></a>
When true, indicates that an upgrade eligibility check was performed.
Type: Boolean

 ** [TargetVersion](#API_UpgradeDomain_ResponseSyntax) **   <a name="opensearchservice-UpgradeDomain-response-TargetVersion"></a>
OpenSearch or Elasticsearch version that the domain was upgraded to.
Type: String
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`

 ** [UpgradeId](#API_UpgradeDomain_ResponseSyntax) **   <a name="opensearchservice-UpgradeDomain-response-UpgradeId"></a>
The unique identifier of the domain upgrade.
Type: String

## Errors
<a name="API_UpgradeDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpgradeDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpgradeDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpgradeDomain)
