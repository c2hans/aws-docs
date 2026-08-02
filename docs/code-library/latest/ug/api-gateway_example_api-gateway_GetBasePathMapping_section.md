---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_example_api-gateway_GetBasePathMapping_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetBasePathMapping` with an AWS SDK or CLI
<a name="api-gateway_example_api-gateway_GetBasePathMapping_section"></a>

The following code examples show how to use `GetBasePathMapping`.

------
#### [ CLI ]

**AWS CLI**
**To get the base path mapping for a custom domain name**
Command:

```
aws apigateway get-base-path-mapping --domain-name {{subdomain.domain.tld}} --base-path {{v1}}
```
Output:

```
{
    "basePath": "v1",
    "restApiId": "1234w4321e",
    "stage": "api"
}
```
+  For API details, see [GetBasePathMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mapping.html) in *AWS CLI Command Reference*.

------
#### [ PHP ]

**SDK for PHP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/apigateway#code-examples).

```
require 'vendor/autoload.php';

use Aws\ApiGateway\ApiGatewayClient;
use Aws\Exception\AwsException;

/* ////////////////////////////////////////////////////////////////////////////
 * Purpose: Gets the base path mapping for a custom domain name in
 * Amazon API Gateway.
 *
 * Prerequisites: A custom domain name in API Gateway. For more information,
 * see "Custom Domain Names" in the Amazon API Gateway Developer Guide.
 *
 * Inputs:
 * - $apiGatewayClient: An initialized AWS SDK for PHP API client for
 *   API Gateway.
 * - $basePath: The base path name that callers must provide as part of the
 *   URL after the domain name.
 * - $domainName: The custom domain name for the base path mapping.
 *
 * Returns: The base path mapping, if available; otherwise, the error message.
 * ///////////////////////////////////////////////////////////////////////// */

function getBasePathMapping($apiGatewayClient, $basePath, $domainName)
{
    try {
        $result = $apiGatewayClient->getBasePathMapping([
            'basePath' => $basePath,
            'domainName' => $domainName,
        ]);
        return 'The base path mapping\'s effective URI is: ' .
            $result['@metadata']['effectiveUri'];
    } catch (AwsException $e) {
        return 'Error: ' . $e['message'];
    }
}

function getsTheBasePathMapping()
{
    $apiGatewayClient = new ApiGatewayClient([
        'profile' => 'default',
        'region' => 'us-east-1',
        'version' => '2015-07-09'
    ]);

    echo getBasePathMapping($apiGatewayClient, '(none)', 'example.com');
}

// Uncomment the following line to run this code in an AWS account.
// getsTheBasePathMapping();
```
+  For API details, see [GetBasePathMapping](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetBasePathMapping) in *AWS SDK for PHP API Reference*.

------
