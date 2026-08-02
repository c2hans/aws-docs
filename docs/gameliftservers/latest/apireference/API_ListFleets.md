---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListFleets.html
---

# ListFleets
<a name="API_ListFleets"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves a collection of fleet resources in an AWS Region. You can filter the result set to find only those fleets that are deployed with a specific build or script. For fleets that have multiple locations, this operation retrieves fleets based on their home Region only.

You can use operation in the following ways:
+ To get a list of all fleets in a Region, don't provide a build or script identifier.
+ To get a list of all fleets where a specific game build is deployed, provide the build ID.
+ To get a list of all Amazon GameLift Servers Realtime fleets with a specific configuration script, provide the script ID.

Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, this operation returns a list of fleet IDs that match the request parameters. A NextToken value is also returned if there are more result pages to retrieve.

**Note**
Fleet IDs are returned in no particular order.

## Request Syntax
<a name="API_ListFleets_RequestSyntax"></a>

```
{
   "BuildId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "ScriptId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BuildId](#API_ListFleets_RequestSyntax) **   <a name="gameliftservers-ListFleets-request-BuildId"></a>
A unique identifier for the build to request fleets for. Use this parameter to return only fleets using a specified build. Use either the build ID or ARN value.
Type: String
Pattern: `^build-\S+|^arn:.*:build\/build-\S+`
Required: No

 ** [Limit](#API_ListFleets_RequestSyntax) **   <a name="gameliftservers-ListFleets-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListFleets_RequestSyntax) **   <a name="gameliftservers-ListFleets-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ScriptId](#API_ListFleets_RequestSyntax) **   <a name="gameliftservers-ListFleets-request-ScriptId"></a>
A unique identifier for the Realtime script to request fleets for. Use this parameter to return only fleets using a specified script. Use either the script ID or ARN value.
Type: String
Pattern: `^script-\S+|^arn:.*:script\/script-\S+`
Required: No

## Response Syntax
<a name="API_ListFleets_ResponseSyntax"></a>

```
{
   "FleetIds": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetIds](#API_ListFleets_ResponseSyntax) **   <a name="gameliftservers-ListFleets-response-FleetIds"></a>
A set of fleet IDs that match the list request.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

 ** [NextToken](#API_ListFleets_ResponseSyntax) **   <a name="gameliftservers-ListFleets-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_ListFleets_Examples"></a>

### List fleets in a Region
<a name="API_ListFleets_Example_1"></a>

This example retrieves the fleet IDs of all fleets with their home Region in the currently selected Region. It uses the pagination parameters to retrieve two fleet IDs at a time. The example response includes a `NextToken`, which indicates that there are still more results to retrieve.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListFleets_Example_1_Request"></a>

```
{
    "Limit": 2,
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE1"
}
```

#### Sample Response
<a name="API_ListFleets_Example_1_Response"></a>

```
{
    "FleetIds": [
        "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa"
    ],
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2"
}
```

### List all fleets in a Region with a specific build or script
<a name="API_ListFleets_Example_2"></a>

This example retrieves the IDs of fleets in the currently selected Region that are deployed with a specified game build. If you're working with Realtime Servers, you can opt to provide a script ID in place of a build ID. This example does not specify the limit parameter, so results can include up to 16 fleet IDs.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListFleets_Example_2_Request"></a>

```
{
    "Build": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
}
```

#### Sample Response
<a name="API_ListFleets_Example_2_Response"></a>

```
{
    "FleetIds": ["fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"]
}
```

## See Also
<a name="API_ListFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListFleets)
