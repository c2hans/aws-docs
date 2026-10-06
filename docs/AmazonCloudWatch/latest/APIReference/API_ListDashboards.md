---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html
---

# ListDashboards
<a name="API_ListDashboards"></a>

Returns a list of the dashboards for your account. If you include `DashboardNamePrefix`, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed.

 `ListDashboards` returns up to 1000 results on one page. If there are more than 1000 dashboards, you can call `ListDashboards` again and include the value you received for `NextToken` in the first call, to receive the next 1000 results.

You might have recently enabled an [opt-in Region (Region that is disabled by default)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion) for your account. In that Region, `ListDashboards` can return an access denied error for up to 24 hours after you enable the Region. This delay occurs while dashboard data propagates. The error does not indicate a problem with your permissions. Because dashboards are global, you can call `ListDashboards` in any other enabled Region, or retry after propagation completes.

## Request Syntax
<a name="API_ListDashboards_RequestSyntax"></a>

```
{
   "DashboardNamePrefix": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDashboards_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DashboardNamePrefix](#API_ListDashboards_RequestSyntax) **   <a name="ACW-ListDashboards-request-DashboardNamePrefix"></a>
If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, ".", "-", and "\_".
Type: String
Required: No

 ** [NextToken](#API_ListDashboards_RequestSyntax) **   <a name="ACW-ListDashboards-request-NextToken"></a>
The token returned by a previous call to indicate that there is more data available.
Type: String
Required: No

## Response Syntax
<a name="API_ListDashboards_ResponseSyntax"></a>

```
{
   "DashboardEntries": [
      {
         "DashboardArn": "string",
         "DashboardName": "string",
         "LastModified": number,
         "Size": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDashboards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DashboardEntries](#API_ListDashboards_ResponseSyntax) **   <a name="ACW-ListDashboards-response-DashboardEntries"></a>
The list of matching dashboards.
Type: Array of [DashboardEntry](API_DashboardEntry.md) objects

 ** [NextToken](#API_ListDashboards_ResponseSyntax) **   <a name="ACW-ListDashboards-response-NextToken"></a>
The token that marks the start of the next batch of returned results.
Type: String

## Errors
<a name="API_ListDashboards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Request processing has failed due to some unknown error, exception, or failure.
 ** Message **

HTTP Status Code: 500

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ListDashboards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListDashboards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListDashboards)
