---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetInstanceAccess.html
---

# GetInstanceAccess
<a name="API_GetInstanceAccess"></a>

 **This API works with the following fleet types:** EC2

Requests authorization to remotely connect to an instance in an Amazon GameLift Servers managed fleet. Use this operation to connect to instances with game servers that use Amazon GameLift Servers server SDK 4.x or earlier. To connect to instances with game servers that use server SDK 5.x or later, call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess).

To request access to an instance, specify IDs for the instance and the fleet it belongs to. You can retrieve instance IDs for a fleet by calling [DescribeInstances](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeInstances.html) with the fleet ID.

If successful, this operation returns an IP address and credentials. The returned credentials match the operating system of the instance, as follows:
+ For a Windows instance: returns a user name and secret (password) for use with a Windows Remote Desktop client.
+ For a Linux instance: returns a user name and secret (RSA private key) for use with an SSH client. You must save the secret to a `.pem` file. If you're using the AWS CLI, see the example [ Get credentials for a Linux instance](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess.html#API_GetInstanceAccess_Examples) for tips on automatically saving the secret to a `.pem` file.

 **Learn more**

 [Remotely connect to fleet instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html)

 [Debug fleet issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_GetInstanceAccess_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetInstanceAccess_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_GetInstanceAccess_RequestSyntax) **   <a name="gameliftservers-GetInstanceAccess-request-FleetId"></a>
A unique identifier for the fleet that contains the instance you want to access. You can request access to instances in EC2 fleets with the following statuses: `ACTIVATING`, `ACTIVE`, or `ERROR`. Use either a fleet ID or an ARN value.
You can access fleets in `ERROR` status for a short period of time before Amazon GameLift Servers deletes them.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [InstanceId](#API_GetInstanceAccess_RequestSyntax) **   <a name="gameliftservers-GetInstanceAccess-request-InstanceId"></a>
A unique identifier for the instance you want to access. You can access an instance in any status.
Type: String
Pattern: `[a-zA-Z0-9\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetInstanceAccess_ResponseSyntax"></a>

```
{
   "InstanceAccess": {
      "Credentials": {
         "Secret": "string",
         "UserName": "string"
      },
      "FleetId": "string",
      "InstanceId": "string",
      "IpAddress": "string",
      "OperatingSystem": "string"
   }
}
```

## Response Elements
<a name="API_GetInstanceAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceAccess](#API_GetInstanceAccess_ResponseSyntax) **   <a name="gameliftservers-GetInstanceAccess-response-InstanceAccess"></a>
The connection information for a fleet instance, including IP address and access credentials.
Type: [InstanceAccess](API_InstanceAccess.md) object

## Errors
<a name="API_GetInstanceAccess_Errors"></a>

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
<a name="API_GetInstanceAccess_Examples"></a>

### Get credentials for a Linux instance
<a name="API_GetInstanceAccess_Example_1"></a>

This example requests a set of credentials to remotely connect to a fleet instance deployed with a Linux Amazon machine image (AMI). The instance is running a game server build with server SDK version 4.02.

When calling `GetInstanceAccess` programmatically, save the returned value of `Secret` (an RSA private key) as a `.pem` file in the proper format. The returned value uses a newline (`\n`) to indicate a line break.

If you're calling `GetInstanceAccess` with the AWS CLI, you can automatically save the RSA private key as a `.pem` file. The CLI syntax in this example saves the secret to a file called `MyPrivateKey.pem`. After saving the private key, you can update the file permissions with the following command:

 `$ chmod 400 MyPrivateKey.pem`

#### Sample Request
<a name="API_GetInstanceAccess_Example_1_Request"></a>

```
    {"FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "InstanceId": "i-11111111a222b333c"
    }

CLI syntax:
    aws gamelift get-instance-access  \
      --fleet-id "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa" \
      --instance-id "i-11111111a222b333c" \
      --query 'InstanceAccess.Credentials.Secret' \
      --output text > MyPrivateKey.pem
```

#### Sample Response
<a name="API_GetInstanceAccess_Example_1_Response"></a>

```
{"InstanceAccess": {
    "Credentials": {
        "Secret": "-----BEGIN RSA PRIVATE KEY-----nEXAMPLEKEYKCAQEAy7WZhaDsrA1W3mRlQtvhwyORRX8gnxgDAfRt/gx42kWXsT4rXE/b5CpSgie/\nvBoU7jLxx92pNHoFnByP+Dc21eyyz6CvjTmWA0JwfWiW5/akH7iO5dSrvC7dQkW2duV5QuUdE0QW\nZ/aNxMniGQE6XAgfwlnXVBwrerrQo+ZWQeqiUwwMkuEbLeJFLhMCvYURpUMSC1oehm449ilx9X1F\nG50TCFeOzfl8dqqCP6GzbPaIjiU19xX/azOR9V+tpUOzEL+wmXnZt3/nHPQ5xvD2OJH67km6SuPW\noPzev/D8V+x4+bHthfSjR9Y7DvQFjfBVwHXigBdtZcU2/wei8D/HYwIDAQABAoIBAGZ1kaEvnrqu\n/uler7vgIn5m7lN5LKw4hJLAIW6tUT/fzvtcHK0SkbQCQXuriHmQ2MQyJX/0kn2NfjLV/ufGxbL1\nmb5qwMGUnEpJaZD6QSSs3kICLwWUYUiGfc0uiSbmJoap/GTLU0W5Mfcv36PaBUNy5p53V6G7hXb2\nbahyWyJNfjLe4M86yd2YK3V2CmK+X/BOsShnJ36+hjrXPPWmV3N9zEmCdJjA+K15DYmhm/tJWSD9\n81oGk9TopEp7CkIfatEATyyZiVqoRq6k64iuM9JkA3OzdXzMQexXVJ1TLZVEH0E7bhlY9d8O1ozR\noQs/FiZNAx2iijCWyv0lpjE73+kCgYEA9mZtyhkHkFDpwrSM1APaL8oNAbbjwEy7Z5Mqfql+lIp1\nYkriL0DbLXlvRAH+yHPRit2hHOjtUNZh4Axv+cpg09qbUI3+43eEy24B7G/Uh+GTfbjsXsOxQx/x\np9otyVwc7hsQ5TA5PZb+mvkJ5OBEKzet9XcKwONBYELGhnEPe7cCgYEA06Vgov6YHleHui9kHuws\nayav0elc5zkxjF9nfHFJRry21R1trw2Vdpn+9g481URrpzWVOEihvm+xTtmaZlSp//lkq75XDwnU\nWA8gkn6O3QE3fq2yN98BURsAKdJfJ5RL1HvGQvTe10HLYYXpJnEkHv+Unl2ajLivWUt5pbBrKbUC\ngYBjbO+OZk0sCcpZ29sbzjYjpIddErySIyRX5gV2uNQwAjLdp9PfN295yQ+BxMBXiIycWVQiw0bH\noMo7yykABY7Ozd5wQewBQ4AdSlWSX4nGDtsiFxWiI5sKuAAeOCbTosy1s8w8fxoJ5Tz1sdoxNeGs\nArq6Wv/G16zQuAE9zK9vvwKBgF+09VI/1wJBirsDGz9whVWfFPrTkJNvJZzYt69qezxlsjgFKshy\nWBhd4xHZtmCqpBPlAymEjr/TOlbxyARmXMnIOWIAnNXMGB4KGSyl1mzSVAoQ+fqR+cJ3d0dyPl1j\njjb0Ed/NY8frlNDxAVHE8BSkdsx2f6ELEyBKJSRr9snRAoGAMrTwYneXzvTskF/S5Fyu0iOegLDa\nNWUH38v/nDCgEpIXD5Hn3qAEcju1IjmbwlvtW+nY2jVhv7UGd8MjwUTNGItdb6nsYqM2asrnF3qS\nVRkAKKKYeGjkpUfVTrW0YFjXkfcrR/V+QFL5OndHAKJXjW7a4ejJLncTzmZSpYzwApc=\n-----END RSA PRIVATE KEY-----",
        "UserName": "gl-user-remote"
    },
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "InstanceId": "i-11111111a222b333c",
    "IpAddress": "192.0.2.0",
    "OperatingSystem": "AMAZON_LINUX_2"
}
```

### Get credentials for a Windows instance
<a name="API_GetInstanceAccess_Example_2"></a>

This example requests a set of credentials to remotely connect to a fleet instance deployed with a Windows Amazon machine image (AMI). The instance is running a game server build with server SDK version 4.02.

#### Sample Request
<a name="API_GetInstanceAccess_Example_2_Request"></a>

```
    {"FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "InstanceId": "i-11111111a222b333c"
    }

CLI syntax:
    aws gamelift get-instance-access \
      --fleet-id "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa" \
      --instance-id "i-11111111a222b333c"
```

#### Sample Response
<a name="API_GetInstanceAccess_Example_2_Response"></a>

```
{"InstanceAccess": {
    "Credentials": {
        "Secret": "aA1bBB2cCCd3EEE",
        "UserName": "gl-user-remote"
    },
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "InstanceId": "i-11111111a222b333c",
    "IpAddress": "192.0.2.0",
    "OperatingSystem": "WIN_2012"
}
```

## See Also
<a name="API_GetInstanceAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/GetInstanceAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GetInstanceAccess)
