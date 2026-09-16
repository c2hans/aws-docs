---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html
---

# ListControls
<a name="API_ListControls"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Returns a list of controls from AWS Audit Manager.

## Request Syntax
<a name="API_ListControls_RequestSyntax"></a>

```
GET /controls?controlCatalogId={{controlCatalogId}}&controlType={{controlType}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListControls_RequestParameters"></a>

The request uses the following URI parameters.

 ** [controlCatalogId](#API_ListControls_RequestSyntax) **   <a name="auditmanager-ListControls-request-uri-controlCatalogId"></a>
A filter that narrows the list of controls to a specific resource from the AWS Control Catalog.
To use this parameter, specify the ARN of the Control Catalog resource. You can specify either a control domain, a control objective, or a common control. For information about how to find the ARNs for these resources, see [`ListDomains`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html), [`ListObjectives`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListObjectives.html), and [`ListCommonControls`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html).
You can only filter by one Control Catalog resource at a time. Specifying multiple resource ARNs isn’t currently supported. If you want to filter by more than one ARN, we recommend that you run the `ListControls` operation separately for each ARN.
Alternatively, specify `UNCATEGORIZED` to list controls that aren't mapped to a Control Catalog resource. For example, this operation might return a list of custom controls that don't belong to any control domain or control objective.
Length Constraints: Minimum length of 13. Maximum length of 2048.
Pattern: `^arn:.*:controlcatalog:.*|UNCATEGORIZED`

 ** [controlType](#API_ListControls_RequestSyntax) **   <a name="auditmanager-ListControls-request-uri-controlType"></a>
A filter that narrows the list of controls to a specific type.
Valid Values: `Standard | Custom | Core`
Required: Yes

 ** [maxResults](#API_ListControls_RequestSyntax) **   <a name="auditmanager-ListControls-request-uri-maxResults"></a>
The maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListControls_RequestSyntax) **   <a name="auditmanager-ListControls-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Request Body
<a name="API_ListControls_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListControls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "controlMetadataList": [
      {
         "arn": "string",
         "controlSources": "string",
         "createdAt": number,
         "id": "string",
         "lastUpdatedAt": number,
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [controlMetadataList](#API_ListControls_ResponseSyntax) **   <a name="auditmanager-ListControls-response-controlMetadataList"></a>
 A list of metadata that the `ListControls` API returns for each control.
Type: Array of [ControlMetadata](API_ControlMetadata.md) objects

 ** [nextToken](#API_ListControls_ResponseSyntax) **   <a name="auditmanager-ListControls-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Errors
<a name="API_ListControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_ListControls_Examples"></a>

### Retrieving a list of custom controls
<a name="API_ListControls_Example_1"></a>

This shows a sample response that the `ListControls` operation might return if you had three custom controls.

#### Sample Response
<a name="API_ListControls_Example_1_Response"></a>

```
{
    "controlMetadataList": [
        {
            "arn": "arn:aws:auditmanager:us-east-1:111122223333:control/a1b2c3d4-5678-90ab-cdef-example11111",
            "id": "a1b2c3d4-5678-90ab-cdef-example11111",
            "name": "Example custom control",
            "controlSources": "AWS API calls, AWS Config, Manual",
            "createdAt": "2022-03-28T18:08:24.446000-07:00",
            "lastUpdatedAt": "2022-03-28T18:08:24.446000-07:00"
        },
        {
            "arn": "arn:aws:auditmanager:us-east-1:111122223333:control/a1b2c3d4-5678-90ab-cdef-example22222",
            "id": "a1b2c3d4-5678-90ab-cdef-example22222",
            "name": "Another custom control",
            "controlSources": "AWS API calls, AWS Config, Manual",
            "createdAt": "2022-03-28T17:45:15.622000-07:00",
            "lastUpdatedAt": "2022-03-28T18:06:56.171000-07:00"
        },
        {
            "arn": "arn:aws:auditmanager:us-east-1:111122223333:control/a1b2c3d4-5678-90ab-cdef-example33333",
            "id": "a1b2c3d4-5678-90ab-cdef-example33333",
            "name": "Custom control - CloudTrail Volume Events",
            "controlSources": "AWS CloudTrail",
            "createdAt": "2021-03-08T11:31:12.468000-08:00",
            "lastUpdatedAt": "2022-01-10T14:13:37.979000-08:00"
        }
    ]
}
```

### Retrieving a list of core controls
<a name="API_ListControls_Example_2"></a>

This example shows how you can use the `ListControls` operation to return a filtered list of core controls that fall under a specific control domain (*Asset management*).

**To retrieve a list of core controls**

1. Use the [`ListDomains`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html) operation to see the control domains that you can use as filters. Find the control domain that you want to use as a filter (*Asset management*), and take note of its ARN.

1. Use the `ListControls` operation and use the following attributes as filters:
   + Use `ControlType` and specify `Core` as the value.
   + Use `ControlCatalogId` and specify the control domain ARN that you got from step 1.

The sample request uses the following ARN as a filter:
+ This ARN represents the Asset management control domain: `arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq`

The sample response shows the results that the `ListControls` operation might return if two core controls matched the domain criteria of *Asset management*.

#### Sample Request
<a name="API_ListControls_Example_2_Request"></a>

```
aws auditmanager list-controls --controlType Core --controlCatalogId "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq"
```

#### Sample Response
<a name="API_ListControls_Example_2_Response"></a>

```
{
   "controlMetadataList": [
    {
        "arn": "arn:aws:auditmanager:us-west-2::control/a1b2c3d4-5678-90ab-cdef-example11111",
        "controlSources": "Manual",
        "createdAt": 1.681511681787E9,
        "id": "a1b2c3d4-5678-90ab-cdef-example11111",
        "lastUpdatedAt": 1.681511681788E9,
        "name": "164.312(a)(2)(iii)"
    }, {
        "arn": "arn:aws:auditmanager:us-west-2::control/a1b2c3d4-5678-90ab-cdef-example22222",
        "controlSources": "AWS API calls, AWS Config, AWS Security Hub",
        "createdAt": 1.681511681787E9,
        "id": "a1b2c3d4-5678-90ab-cdef-example22222",
        "lastUpdatedAt": 1.681511681788E9,
        "name": "164.312(c)(1)"
   } ],
   "nextToken": "string"
}
```

## See Also
<a name="API_ListControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/ListControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ListControls)
