---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.html
---

# DescribeHomeRegionControls
<a name="API_DescribeHomeRegionControls"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

This API permits filtering on the `ControlId` and `HomeRegion` fields.

## Request Syntax
<a name="API_DescribeHomeRegionControls_RequestSyntax"></a>

```
{
   "ControlId": "{{string}}",
   "HomeRegion": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Target": {
      "Id": "{{string}}",
      "Type": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DescribeHomeRegionControls_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ControlId](#API_DescribeHomeRegionControls_RequestSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-request-ControlId"></a>
The `ControlID` is a unique identifier string of your `HomeRegionControl` object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^hrc-[a-z0-9]{12}$`
Required: No

 ** [HomeRegion](#API_DescribeHomeRegionControls_RequestSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-request-HomeRegion"></a>
The name of the home region you'd like to view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([a-z]+)-([a-z]+)-([0-9]+)$`
Required: No

 ** [MaxResults](#API_DescribeHomeRegionControls_RequestSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-request-MaxResults"></a>
The maximum number of filtering results to display per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeHomeRegionControls_RequestSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-request-NextToken"></a>
If a `NextToken` was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in `NextToken`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`
Required: No

 ** [Target](#API_DescribeHomeRegionControls_RequestSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-request-Target"></a>
The target parameter specifies the identifier to which the home region is applied, which is always of type `ACCOUNT`. It applies the home region to the current `ACCOUNT`.
Type: [Target](API_Target.md) object
Required: No

## Response Syntax
<a name="API_DescribeHomeRegionControls_ResponseSyntax"></a>

```
{
   "HomeRegionControls": [
      {
         "ControlId": "string",
         "HomeRegion": "string",
         "RequestedTime": number,
         "Target": {
            "Id": "string",
            "Type": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeHomeRegionControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HomeRegionControls](#API_DescribeHomeRegionControls_ResponseSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-response-HomeRegionControls"></a>
An array that contains your `HomeRegionControl` objects.
Type: Array of [HomeRegionControl](API_HomeRegionControl.md) objects
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_DescribeHomeRegionControls_ResponseSyntax) **   <a name="migrationhubhomeregion-DescribeHomeRegionControls-response-NextToken"></a>
If a `NextToken` was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in `NextToken`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

## Errors
<a name="API_DescribeHomeRegionControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerError **
Exception raised when an internal, configuration, or dependency error is encountered.
HTTP Status Code: 500

 ** InvalidInputException **
Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.
HTTP Status Code: 400

 ** ServiceUnavailableException **
Exception raised when a request fails due to temporary unavailability of the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

## See Also
<a name="API_DescribeHomeRegionControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhub-config-2019-06-30/DescribeHomeRegionControls)
