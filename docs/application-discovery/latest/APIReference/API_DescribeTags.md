---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeTags.html
---

# DescribeTags
<a name="API_DescribeTags"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Retrieves a list of configuration items that have tags as specified by the key-value pairs, name and value, passed to the optional parameter `filters`.

There are three valid tag filter names:
+ tagKey
+ tagValue
+ configurationId

Also, all configuration items associated with your user that have tags can be listed if you call `DescribeTags` as is without passing any parameters.

## Request Syntax
<a name="API_DescribeTags_RequestSyntax"></a>

```
{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeTags_RequestSyntax) **   <a name="DiscServ-DescribeTags-request-filters"></a>
You can filter the list using a *key*-*value* format. You can separate these items by using logical operators. Allowed filters include `tagKey`, `tagValue`, and `configurationId`.
Type: Array of [TagFilter](API_TagFilter.md) objects
Required: No

 ** [maxResults](#API_DescribeTags_RequestSyntax) **   <a name="DiscServ-DescribeTags-request-maxResults"></a>
The total number of items to return in a single page of output. The maximum value is 100.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeTags_RequestSyntax) **   <a name="DiscServ-DescribeTags-request-nextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeTags_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tags": [
      {
         "configurationId": "string",
         "configurationType": "string",
         "key": "string",
         "timeOfCreation": number,
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeTags_ResponseSyntax) **   <a name="DiscServ-DescribeTags-response-nextToken"></a>
The call returns a token. Use this token to get the next set of results.
Type: String

 ** [tags](#API_DescribeTags_ResponseSyntax) **   <a name="DiscServ-DescribeTags-response-tags"></a>
Depending on the input, this is a list of configuration items tagged with a specific tag, or a list of tags for a specific configuration item.
Type: Array of [ConfigurationTag](API_ConfigurationTag.md) objects

## Errors
<a name="API_DescribeTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified configuration ID was not located. Verify the configuration ID and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_DescribeTags_Examples"></a>

### Describe tags that have a particular value
<a name="API_DescribeTags_Example_1"></a>

The following example lists configuration items associated with an agent installed on a linux server. This is done by passing object array values to the parameter `filters` where `name` is "tagValue" and `value` is "agent on linux server". This results in a descriptive response that lists configuration item details where the tag value is equal to the value specified in the request.

#### Sample Request
<a name="API_DescribeTags_Example_1_Request"></a>

```
{
"filters": [
       {
         "name": "tagValue",
         "values": [ "agent on linux server" ]
      }
   ]
}
```

#### Sample Response
<a name="API_DescribeTags_Example_1_Response"></a>

```
{
    "tags": [
        {
            "configurationType": "SERVER",
            "configurationId": "d-server-0c269e353e6d1fb4c",
            "key": "dp2",
            "value": "agent on linux server",
            "timeOfCreation": 1519674610.0
        }
    ],
    "nextToken": "0039038d504694533"
}
```

## See Also
<a name="API_DescribeTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeTags)
