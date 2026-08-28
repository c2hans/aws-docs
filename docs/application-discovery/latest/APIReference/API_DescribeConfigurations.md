---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeConfigurations.html
---

# DescribeConfigurations
<a name="API_DescribeConfigurations"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Retrieves attributes for a list of configuration item IDs.

**Note**
All of the supplied IDs must be for the same asset type from one of the following:
server
application
process
connection
Output fields are specific to the asset type specified. For example, the output for a *server* configuration item includes a list of attributes about the server, such as host name, operating system, number of network cards, etc.
For a complete list of outputs for each asset type, see [Using the DescribeConfigurations Action](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#DescribeConfigurations) in the * AWS Application Discovery Service User Guide*.

## Request Syntax
<a name="API_DescribeConfigurations_RequestSyntax"></a>

```
{
   "configurationIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [configurationIds](#API_DescribeConfigurations_RequestSyntax) **   <a name="DiscServ-DescribeConfigurations-request-configurationIds"></a>
One or more configuration IDs.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

## Response Syntax
<a name="API_DescribeConfigurations_ResponseSyntax"></a>

```
{
   "configurations": [
      {
         "string" : "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurations](#API_DescribeConfigurations_ResponseSyntax) **   <a name="DiscServ-DescribeConfigurations-response-configurations"></a>
A key in the response map. The value is an array of data.
Type: Array of string to string maps
Key Length Constraints: Maximum length of 10000.
Key Pattern: `[\s\S]*`
Value Length Constraints: Maximum length of 10000.
Value Pattern: `[\s\S]*`

## Errors
<a name="API_DescribeConfigurations_Errors"></a>

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

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_DescribeConfigurations_Examples"></a>

### Describe configurations
<a name="API_DescribeConfigurations_Example_1"></a>

The following example queries configuration descriptions of two applications as specified by the values passed to the parameter `configurationIds` in the request. Note that the configuration ID's passed meet the requirement that they represent the same asset type, in this example, *application*.

#### Sample Request
<a name="API_DescribeConfigurations_Example_1_Request"></a>

```
{
    "configurationIds": [
	      "d-application-0282ccd1ba7c211ca",
	      "d-application-034219054305e4a34"
	  ]
}
```

#### Sample Response
<a name="API_DescribeConfigurations_Example_1_Response"></a>

```
{
    "configurations": [
        {
            "application.configurationId": "d-application-0282ccd1ba7c211ca",
            "application.description": "ads CreateApplication",
            "application.lastModifiedTime": "2018-02-27 00:48:16.0",
            "application.name": "adsdp2",
            "application.serverCount": "2",
            "application.timeOfCreation": "2018-02-27 00:48:16.0"
        },
        {
            "application.configurationId": "d-application-034219054305e4a34",
            "application.description": "ads CreateApplication place holder app",
            "application.lastModifiedTime": "2018-02-27 23:33:32.0",
            "application.name": "adsdp2_ph1",
            "application.serverCount": "0",
            "application.timeOfCreation": "2018-02-27 23:33:32.0"
        }
    ]
}
```

## See Also
<a name="API_DescribeConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
