---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicies.html
---

# GetLifecyclePolicies
<a name="API_GetLifecyclePolicies"></a>

Gets summary information about all or the specified data lifecycle policies.

To get complete information about a policy, use [GetLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicy.html).

## Request Syntax
<a name="API_GetLifecyclePolicies_RequestSyntax"></a>

```
GET /policies?defaultPolicyType={{DefaultPolicyType}}&policyIds={{PolicyIds}}&resourceTypes={{ResourceTypes}}&state={{State}}&tagsToAdd={{TagsToAdd}}&targetTags={{TargetTags}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLifecyclePolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DefaultPolicyType](#API_GetLifecyclePolicies_RequestSyntax) **   <a name="dlm-GetLifecyclePolicies-request-uri-DefaultPolicyType"></a>
 **[Default policies only]** Specifies the type of default policy to get. Specify one of the following:
+  `VOLUME` - To get only the default policy for EBS snapshots
+  `INSTANCE` - To get only the default policy for EBS-backed AMIs
+  `ALL` - To get all default policies
Valid Values: `VOLUME | INSTANCE | ALL`

 ** [PolicyIds](#API_GetLifecyclePolicies_RequestSyntax) **   <a name="dlm-GetLifecyclePolicies-request-uri-PolicyIds"></a>
The identifiers of the data lifecycle policies.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`

 ** [ResourceTypes](#API_GetLifecyclePolicies_RequestSyntax) **   <a name="dlm-GetLifecyclePolicies-request-uri-ResourceTypes"></a>
The resource type.
Array Members: Fixed number of 1 item.
Valid Values: `VOLUME | INSTANCE`

 ** [State](#API_GetLifecyclePolicies_RequestSyntax) **   <a name="dlm-GetLifecyclePolicies-request-uri-State"></a>
The activation state.
Valid Values: `ENABLED | DISABLED | ERROR`

 ** [TagsToAdd](#API_GetLifecyclePolicies_RequestSyntax) **   <a name="dlm-GetLifecyclePolicies-request-uri-TagsToAdd"></a>
The tags to add to objects created by the policy.
Tags are strings in the format `key=value`.
These user-defined tags are added in addition to the AWS-added lifecycle tags.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{all}]*`

 ** [TargetTags](#API_GetLifecyclePolicies_RequestSyntax) **   <a name="dlm-GetLifecyclePolicies-request-uri-TargetTags"></a>
The target tag for a policy.
Tags are strings in the format `key=value`.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{all}]*`

## Request Body
<a name="API_GetLifecyclePolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLifecyclePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policies": [
      {
         "DefaultPolicy": boolean,
         "Description": "string",
         "PolicyId": "string",
         "PolicyType": "string",
         "State": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetLifecyclePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policies](#API_GetLifecyclePolicies_ResponseSyntax) **   <a name="dlm-GetLifecyclePolicies-response-Policies"></a>
Summary information about the lifecycle policies.
Type: Array of [LifecyclePolicySummary](API_LifecyclePolicySummary.md) objects

## Errors
<a name="API_GetLifecyclePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service failed in an unexpected way.
HTTP Status Code: 500

 ** InvalidRequestException **
Bad request. The request is missing required parameters or has invalid parameters.
 ** MutuallyExclusiveParameters **
The request included parameters that cannot be provided together.
 ** RequiredParameters **
The request omitted one or more required parameters.
HTTP Status Code: 400

 ** LimitExceededException **
The request failed because a limit was exceeded.
 ** ResourceType **
Value is the type of resource for which a limit was exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
A requested resource was not found.
 ** ResourceIds **
Value is a list of resource IDs that were not found.
 ** ResourceType **
Value is the type of resource that was not found.
HTTP Status Code: 404

## See Also
<a name="API_GetLifecyclePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dlm-2018-01-12/GetLifecyclePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/GetLifecyclePolicies)
