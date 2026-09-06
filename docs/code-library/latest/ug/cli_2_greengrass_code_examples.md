---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_greengrass_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS IoT Greengrass examples using AWS CLI
<a name="cli_2_greengrass_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT Greengrass.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `associate-role-to-group`
<a name="greengrass_AssociateRoleToGroup_cli_2_topic"></a>

The following code example shows how to use `associate-role-to-group`.

**AWS CLI**
**To associate a role with a Greengrass group**
The following `associate-role-to-group` example associates the specified IAM role with a Greengrass group. The group role is used by local Lambda functions and connectors to access AWS services. For example, your group role might grant permissions required for CloudWatch Logs integration.

```
aws greengrass associate-role-to-group \
    --group-id {{2494ee3f-7f8a-4e92-a78b-d205f808b84b}} \
    --role-arn {{arn:aws:iam::123456789012:role/GG-Group-Role}}
```
Output:

```
{
    "AssociatedAt": "2019-09-10T20:03:30Z"
}
```
For more information, see [Configure the Group Role](https://docs.aws.amazon.com/greengrass/latest/developerguide/config-iam-roles.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [AssociateRoleToGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/associate-role-to-group.html) in *AWS CLI Command Reference*.

### `associate-service-role-to-account`
<a name="greengrass_AssociateServiceRoleToAccount_cli_2_topic"></a>

The following code example shows how to use `associate-service-role-to-account`.

**AWS CLI**
**To associate a service role with your AWS account**
The following `associate-service-role-to-account` example associates an IAM service role, specified by its ARN, with AWS IoT Greengrass in your AWS account. You must have previously created the service role in IAM, and you must associate a policy document with it that allows AWS IoT Greengrass to assume this role.

```
aws greengrass associate-service-role-to-account \
    --role-arn {{"arn:aws:iam::123456789012:role/service-role/Greengrass_ServiceRole"}}
```
Output:

```
{
    "AssociatedAt": "2019-06-25T18:12:45Z"
}
```
For more information, see [Greengrass Service Role](https://docs.aws.amazon.com/greengrass/latest/developerguide/service-role.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [AssociateServiceRoleToAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/associate-service-role-to-account.html) in *AWS CLI Command Reference*.

### `create-connector-definition-version`
<a name="greengrass_CreateConnectorDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-connector-definition-version`.

**AWS CLI**
**To create a connector definition version**
The following `create-connector-definition-version` example creates a connector definition version and associates it with the specified connector definition. All connectors in a version define values for their parameters.

```
aws greengrass create-connector-definition-version \
    --connector-definition-id {{"55d0052b-0d7d-44d6-b56f-21867215e118"}} \
    --connectors "[{\"Id\": \"MyTwilioNotificationsConnector\", \"ConnectorArn\": \"arn:aws:greengrass:us-west-2::/connectors/TwilioNotifications/versions/2\", \"Parameters\": {\"TWILIO_ACCOUNT_SID\": \"AC1a8d4204890840d7fc482aab38090d57\", \"TwilioAuthTokenSecretArn\": \"arn:aws:secretsmanager:us-west-2:123456789012:secret:greengrass-TwilioAuthToken-ntSlp6\", \"TwilioAuthTokenSecretArn-ResourceId\": \"TwilioAuthToken\", \"DefaultFromPhoneNumber\": \"4254492999\"}}]"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/55d0052b-0d7d-44d6-b56f-21867215e118/versions/33f709a0-c825-49cb-9eea-dc8964fbd635",
    "CreationTimestamp": "2019-06-24T20:46:30.134Z",
    "Id": "55d0052b-0d7d-44d6-b56f-21867215e118",
    "Version": "33f709a0-c825-49cb-9eea-dc8964fbd635"
}
```
+  For API details, see [CreateConnectorDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition-version.html) in *AWS CLI Command Reference*.

### `create-connector-definition`
<a name="greengrass_CreateConnectorDefinition_cli_2_topic"></a>

The following code example shows how to use `create-connector-definition`.

**AWS CLI**
**To create a connector definition**
The following `create-connector-definition` example example creates a connector definition and an initial connector definition version. The initial version contains one connector. All connectors in a version define values for their parameters.

```
aws greengrass create-connector-definition \
    --name {{MySNSConnector}} \
    --initial-version "{\"Connectors\": [{\"Id\":\"MySNSConnector\",\"ConnectorArn\":\"arn:aws:greengrass:us-west-2::/connectors/SNS/versions/1\",\"Parameters\": {\"DefaultSNSArn\":\"arn:aws:sns:us-west-2:123456789012:GGConnectorTopic\"}}]}"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
    "CreationTimestamp": "2019-06-19T19:30:01.300Z",
    "Id": "b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
    "LastUpdatedTimestamp": "2019-06-19T19:30:01.300Z",
    "LatestVersion": "63c57963-c7c2-4a26-a7e2-7bf478ea2623",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8/versions/63c57963-c7c2-4a26-a7e2-7bf478ea2623",
    "Name": "MySNSConnector"
}
```
For more information, see [Getting Started with Greengrass Connectors (CLI)](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-cli.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [CreateConnectorDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition.html) in *AWS CLI Command Reference*.

### `create-core-definition-version`
<a name="greengrass_CreateCoreDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-core-definition-version`.

**AWS CLI**
**To create a core definition version**
The following `create-core-definition-version` example creates a core definition version and associates it with the specified core definition. The version can contain one core only. Before you can create a core, you must first create and provision the corresponding AWS IoT thing. This process includes the following `iot` commands, which return the `ThingArn` and `CertificateArn` required for the `create-core-definition-version` command.
Create the AWS IoT thing that corresponds to the core device:

```
aws iot create-thing \
    --thing-name "MyCoreDevice"
```
Output:

```
{
    "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyCoreDevice",
    "thingName": "MyCoreDevice",
    "thingId": "cb419a19-9099-4515-9cec-e9b0e760608a"
}
```
Create public and private keys and the core device certificate for the thing. This example uses the `create-keys-and-certificate` command and requires write permissions to the current directory. Alternatively, you can use the `create-certificate-from-csr` command.

```
aws iot create-keys-and-certificate \
    --set-as-active \
    --certificate-pem-outfile "myCore.cert.pem" \
    --public-key-outfile "myCore.public.key" \
    --private-key-outfile "myCore.private.key"
```
Output:

```
{
    "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz",
    "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDWTCAkGgAwIBATgIUCgq6EGqou6zFqWgIZRndgQEFW+gwDQYJKoZIhvc...KdGewQS\n-----END CERTIFICATE-----\n",
    "keyPair": {
        "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBzrqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqKpRgnn6yq26U3y...wIDAQAB\n-----END PUBLIC KEY-----\n",
        "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIABAKCAQEAqKpRgnn6yq26U3yt5YFZquyukfRjbMXDcNOK4rMCxDR...fvY4+te\n-----END RSA PRIVATE KEY-----\n"
    },
    "certificateId": "123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz"
}
```
Create an AWS IoT policy that allows `iot` and `greengrass` actions. For simplicity, the following policy allows actions on all resources, but your policy should be more restrictive.

```
aws iot create-policy \
    --policy-name "Core_Devices" \
    --policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}"
```
Output:

```
{
    "policyName": "Core_Devices",
    "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/Core_Devices",
    "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}",
    "policyVersionId": "1"
}
```
Attach the policy to the certificate:

```
aws iot attach-policy \
    --policy-name "Core_Devices" \
    --target "arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz"
```
This command produces no output.
Attach the thing to the certificate:

```
aws iot attach-thing-principal \
    --thing-name "MyCoreDevice" \
    --principal "arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz"
```
This command produces no output.
Create the core definition version:

```
aws greengrass create-core-definition-version \
    --core-definition-id "582efe12-b05a-409e-9a24-a2ba1bcc4a12" \
    --cores "[{\"Id\":\"MyCoreDevice\",\"ThingArn\":\"arn:aws:iot:us-west-2:123456789012:thing/MyCoreDevice\",\"CertificateArn\":\"arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz\",\"SyncShadow\":true}]"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/582efe12-b05a-409e-9a24-a2ba1bcc4a12/versions/3fdc1190-2ce5-44de-b98b-eec8f9571014",
    "Version": "3fdc1190-2ce5-44de-b98b-eec8f9571014",
    "CreationTimestamp": "2019-09-18T00:15:09.838Z",
    "Id": "582efe12-b05a-409e-9a24-a2ba1bcc4a12"
}
```
For more information, see [Configure the AWS IoT Greengrass Core](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-core.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateCoreDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-core-definition-version.html) in *AWS CLI Command Reference*.

### `create-core-definition`
<a name="greengrass_CreateCoreDefinition_cli_2_topic"></a>

The following code example shows how to use `create-core-definition`.

**AWS CLI**
**Example 1: To create an empty core definition**
The following `create-core-definition` example creates an empty (no initial version) Greengrass core definition. Before the core is usable, you must use the `create-core-definition-version` command to provide the other parameters for the core.

```
aws greengrass create-core-definition \
    --name {{cliGroup_Core}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/b5c08008-54cb-44bd-9eec-c121b04283b5",
    "CreationTimestamp": "2019-06-25T18:23:22.106Z",
    "Id": "b5c08008-54cb-44bd-9eec-c121b04283b5",
    "LastUpdatedTimestamp": "2019-06-25T18:23:22.106Z",
    "Name": "cliGroup_Core"
}
```
**Example 2: To create a core definition with an initial version**
The following `create-core-definition` example creates a core definition that contains an initial core definition version. The version can contain one core only. Before you can create a core, you must first create and provision the corresponding AWS IoT thing. This process includes the following `iot` commands, which return the `ThingArn` and `CertificateArn` required for the `create-core-definition` command.
Create the AWS IoT thing that corresponds to the core device:

```
aws iot create-thing \
    --thing-name "MyCoreDevice"
```
Output:

```
{
    "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyCoreDevice",
    "thingName": "MyCoreDevice",
    "thingId": "cb419a19-9099-4515-9cec-e9b0e760608a"
}
```
Create public and private keys and the core device certificate for the thing. This example uses the `create-keys-and-certificate` command and requires write permissions to the current directory. Alternatively, you can use the `create-certificate-from-csr` command.

```
aws iot create-keys-and-certificate \
    --set-as-active \
    --certificate-pem-outfile "myCore.cert.pem" \
    --public-key-outfile "myCore.public.key" \
    --private-key-outfile "myCore.private.key"
```
Output:

```
{
    "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz",
    "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDWTCAkGgAwIBATgIUCgq6EGqou6zFqWgIZRndgQEFW+gwDQYJKoZIhvc...KdGewQS\n-----END CERTIFICATE-----\n",
    "keyPair": {
        "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBzrqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqKpRgnn6yq26U3y...wIDAQAB\n-----END PUBLIC KEY-----\n",
        "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIABAKCAQEAqKpRgnn6yq26U3yt5YFZquyukfRjbMXDcNOK4rMCxDR...fvY4+te\n-----END RSA PRIVATE KEY-----\n"
    },
    "certificateId": "123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz"
}
```
Create an AWS IoT policy that allows `iot` and `greengrass` actions. For simplicity, the following policy allows actions on all resources, but your policy should be more restrictive.

```
aws iot create-policy \
    --policy-name "Core_Devices" \
    --policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}"
```
Output:

```
{
    "policyName": "Core_Devices",
    "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/Core_Devices",
    "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}",
    "policyVersionId": "1"
}
```
Attach the policy to the certificate:

```
aws iot attach-policy \
    --policy-name "Core_Devices" \
    --target "arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz"
```
This command produces no output.
Attach the thing to the certificate:

```
aws iot attach-thing-principal \
    --thing-name "MyCoreDevice" \
    --principal "arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz"
```
This command produces no output.
Create the core definition:

```
aws greengrass create-core-definition \
    --name "MyCores" \
    --initial-version "{\"Cores\":[{\"Id\":\"MyCoreDevice\",\"ThingArn\":\"arn:aws:iot:us-west-2:123456789012:thing/MyCoreDevice\",\"CertificateArn\":\"arn:aws:iot:us-west-2:123456789012:cert/123a15ec415668c2349a76170b64ac0878231c1e21ec83c10e92a1EXAMPLExyz\",\"SyncShadow\":true}]}"
```
Output:

```
{
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/582efe12-b05a-409e-9a24-a2ba1bcc4a12/versions/cc87b5b3-8f4b-465d-944c-1d6de5dbfcdb",
    "Name": "MyCores",
    "LastUpdatedTimestamp": "2019-09-18T00:11:06.197Z",
    "LatestVersion": "cc87b5b3-8f4b-465d-944c-1d6de5dbfcdb",
    "CreationTimestamp": "2019-09-18T00:11:06.197Z",
    "Id": "582efe12-b05a-409e-9a24-a2ba1bcc4a12",
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/582efe12-b05a-409e-9a24-a2ba1bcc4a12"
}
```
For more information, see [Configure the AWS IoT Greengrass Core](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-core.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateCoreDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-core-definition.html) in *AWS CLI Command Reference*.

### `create-deployment`
<a name="greengrass_CreateDeployment_cli_2_topic"></a>

The following code example shows how to use `create-deployment`.

**AWS CLI**
**To create a deployment for a version of a Greengrass group**
The following `create-deployment` example deploys the specified version of a Greengrass group.

```
aws greengrass create-deployment \
    --deployment-type {{NewDeployment}} \
    --group-id {{"ce2e7d01-3240-4c24-b8e6-f6f6e7a9eeca"}} \
    --group-version-id {{"dc40c1e9-e8c8-4d28-a84d-a9cad5f599c9"}}
```
Output:

```
{
    "DeploymentArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/ce2e7d01-3240-4c24-b8e6-f6f6e7a9eeca/deployments/bfceb608-4e97-45bc-af5c-460144270308",
    "DeploymentId": "bfceb608-4e97-45bc-af5c-460144270308"
}
```
For more information, see [Getting Started with Connectors (CLI)](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-deployment.html) in *AWS CLI Command Reference*.

### `create-device-definition-version`
<a name="greengrass_CreateDeviceDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-device-definition-version`.

**AWS CLI**
**To create a device definition version**
The following `create-device-definition-version` example creates a device definition version and associates it with the specified device definition. The version defines two devices. Before you can create a Greengrass device, you must first create and provision the corresponding AWS IoT thing. This process includes the following `iot` commands that you must run to get the required information for the Greengrass command:
Create the AWS IoT thing that corresponds to the device:

```
aws iot create-thing \
    --thing-name "InteriorTherm"
```
Output:

```
{
    "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/InteriorTherm",
    "thingName": "InteriorTherm",
    "thingId": "01d4763c-78a6-46c6-92be-7add080394bf"
}
```
Create public and private keys and the device certificate for the thing. This example uses the `create-keys-and-certificate` command and requires write permissions to the current directory. Alternatively, you can use the `create-certificate-from-csr` command:

```
aws iot create-keys-and-certificate \
    --set-as-active \
    --certificate-pem-outfile "myDevice.cert.pem" \
    --public-key-outfile "myDevice.public.key" \
    --private-key-outfile "myDevice.private.key"
```
Output:

```
{
    "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92",
    "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDWTCAkGgAwIBATgIUCgq6EGqou6zFqWgIZRndgQEFW+gwDQYJKoZIhvc...KdGewQS\n-----END CERTIFICATE-----\n",
    "keyPair": {
        "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBzrqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqKpRgnn6yq26U3y...wIDAQAB\n-----END PUBLIC KEY-----\n",
        "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIABAKCAQEAqKpRgnn6yq26U3yt5YFZquyukfRjbMXDcNOK4rMCxDR...fvY4+te\n-----END RSA PRIVATE KEY-----\n"
    },
    "certificateId": "66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92"
}
```
Create an AWS IoT policy that allows `iot` and `greengrass` actions. For simplicity, the following policy allows actions on all resources, but your policy can be more restrictive:

```
aws iot create-policy \
    --policy-name "GG_Devices" \
    --policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}"
```
Output:

```
{
    "policyName": "GG_Devices",
    "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/GG_Devices",
    "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}",
    "policyVersionId": "1"
}
```
Attach the policy to the certificate:

```
aws iot attach-policy \
    --policy-name "GG_Devices" \
    --target "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92"
```
Attach the thing to the certificate

```
aws iot attach-thing-principal \
    --thing-name "InteriorTherm" \
    --principal "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92"
```
After you create and configure the IoT thing as shown above, use the `ThingArn` and `CertificateArn` from the first two commands in the following example.

```
aws greengrass create-device-definition-version \
    --device-definition-id {{"f9ba083d-5ad4-4534-9f86-026a45df1ccd"}} \
    --devices "[{\"Id\":\"InteriorTherm\",\"ThingArn\":\"arn:aws:iot:us-west-2:123456789012:thing/InteriorTherm\",\"CertificateArn\":\"arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92\",\"SyncShadow\":true},{\"Id\":\"ExteriorTherm\",\"ThingArn\":\"arn:aws:iot:us-west-2:123456789012:thing/ExteriorTherm\",\"CertificateArn\":\"arn:aws:iot:us-west-2:123456789012:cert/6c52ce1b47bde88a637e9ccdd45fe4e4c2c0a75a6866f8f63d980ee22fa51e02\",\"SyncShadow\":true}]"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/83c13984-6fed-447e-84d5-5b8aa45d5f71",
    "Version": "83c13984-6fed-447e-84d5-5b8aa45d5f71",
    "CreationTimestamp": "2019-09-11T00:15:09.838Z",
    "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd"
}
```
+  For API details, see [CreateDeviceDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-device-definition-version.html) in *AWS CLI Command Reference*.

### `create-device-definition`
<a name="greengrass_CreateDeviceDefinition_cli_2_topic"></a>

The following code example shows how to use `create-device-definition`.

**AWS CLI**
**To create a device definition**
The following `create-device-definition` example creates a device definition that contains an initial device definition version. The initial version defines two devices. Before you can create a Greengrass device, you must first create and provision the corresponding AWS IoT thing. This process includes the following `iot` commands that you must run to get the required information for the Greengrass command:
Create the AWS IoT thing that corresponds to the device:

```
aws iot create-thing \
    --thing-name "InteriorTherm"
```
Output:

```
{
    "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/InteriorTherm",
    "thingName": "InteriorTherm",
    "thingId": "01d4763c-78a6-46c6-92be-7add080394bf"
}
```
Create public and private keys and the device certificate for the thing. This example uses the `create-keys-and-certificate` command and requires write permissions to the current directory. Alternatively, you can use the `create-certificate-from-csr` command:

```
aws iot create-keys-and-certificate \
    --set-as-active \
    --certificate-pem-outfile "myDevice.cert.pem" \
    --public-key-outfile "myDevice.public.key" \
    --private-key-outfile "myDevice.private.key"
```
Output:

```
{
    "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92",
    "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDWTCAkGgAwIBATgIUCgq6EGqou6zFqWgIZRndgQEFW+gwDQYJKoZIhvc...KdGewQS\n-----END CERTIFICATE-----\n",
    "keyPair": {
        "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBzrqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqKpRgnn6yq26U3y...wIDAQAB\n-----END PUBLIC KEY-----\n",
        "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIABAKCAQEAqKpRgnn6yq26U3yt5YFZquyukfRjbMXDcNOK4rMCxDR...fvY4+te\n-----END RSA PRIVATE KEY-----\n"
    },
    "certificateId": "66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92"
}
```
Create an AWS IoT policy that allows `iot` and `greengrass` actions. For simplicity, the following policy allows actions on all resources, but your policy can be more restrictive:

```
aws iot create-policy \
    --policy-name "GG_Devices" \
    --policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}"
```
Output:

```
{
    "policyName": "GG_Devices",
    "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/GG_Devices",
    "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"iot:Publish\",\"iot:Subscribe\",\"iot:Connect\",\"iot:Receive\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"iot:GetThingShadow\",\"iot:UpdateThingShadow\",\"iot:DeleteThingShadow\"],\"Resource\":[\"*\"]},{\"Effect\":\"Allow\",\"Action\":[\"greengrass:*\"],\"Resource\":[\"*\"]}]}",
    "policyVersionId": "1"
}
```
Attach the policy to the certificate:

```
aws iot attach-policy \
    --policy-name "GG_Devices" \
    --target "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92"
```
Attach the thing to the certificate

```
aws iot attach-thing-principal \
    --thing-name "InteriorTherm" \
    --principal "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92"
```
After you create and configure the IoT thing as shown above, use the `ThingArn` and `CertificateArn` from the first two commands in the following example.

```
aws greengrass create-device-definition \
    --name {{"Sensors"}} \
    --initial-version "{\"Devices\":[{\"Id\":\"InteriorTherm\",\"ThingArn\":\"arn:aws:iot:us-west-2:123456789012:thing/InteriorTherm\",\"CertificateArn\":\"arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92\",\"SyncShadow\":true},{\"Id\":\"ExteriorTherm\",\"ThingArn\":\"arn:aws:iot:us-west-2:123456789012:thing/ExteriorTherm\",\"CertificateArn\":\"arn:aws:iot:us-west-2:123456789012:cert/6c52ce1b47bde88a637e9ccdd45fe4e4c2c0a75a6866f8f63d980ee22fa51e02\",\"SyncShadow\":true}]}"
```
Output:

```
{
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/3b5cc510-58c1-44b5-9d98-4ad858ffa795",
    "Name": "Sensors",
    "LastUpdatedTimestamp": "2019-09-11T00:11:06.197Z",
    "LatestVersion": "3b5cc510-58c1-44b5-9d98-4ad858ffa795",
    "CreationTimestamp": "2019-09-11T00:11:06.197Z",
    "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd",
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd"
}
```
+  For API details, see [CreateDeviceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-device-definition.html) in *AWS CLI Command Reference*.

### `create-function-definition-version`
<a name="greengrass_CreateFunctionDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-function-definition-version`.

**AWS CLI**
**To create a version of the function definition**
The following `create-function-definition-version` example creates a new version of the specified function definition. This version specifies a single function whose ID is `Hello-World-function`, allows access to the file system, and specifies a maximum memory size and timeout period.

```
aws greengrass create-function-definition-version \
    --cli-input-json "{\"FunctionDefinitionId\": \"e626e8c9-3b8f-4bf3-9cdc-d26ecdeb9fa3\",\"Functions\": [{\"Id\": \"Hello-World-function\", \"FunctionArn\": \""arn:aws:lambda:us-west-2:123456789012:function:Greengrass_HelloWorld_Counter:gghw-alias"\",\"FunctionConfiguration\": {\"Environment\": {\"AccessSysfs\": true},\"Executable\": \"greengrassHelloWorldCounter.function_handler\",\"MemorySize\": 16000,\"Pinned\": false,\"Timeout\": 25}}]}"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/e626e8c9-3b8f-4bf3-9cdc-d26ecdeb9fa3/versions/74abd1cc-637e-4abe-8684-9a67890f4043",
    "CreationTimestamp": "2019-06-25T22:03:43.376Z",
    "Id": "e626e8c9-3b8f-4bf3-9cdc-d26ecdeb9fa3",
    "Version": "74abd1cc-637e-4abe-8684-9a67890f4043"
}
```
+  For API details, see [CreateFunctionDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition-version.html) in *AWS CLI Command Reference*.

### `create-function-definition`
<a name="greengrass_CreateFunctionDefinition_cli_2_topic"></a>

The following code example shows how to use `create-function-definition`.

**AWS CLI**
**To create a Lambda function definition**
The following `create-function-definition` example creates a Lambda function definition and an initial version by providing a list of Lambda functions (in this case, a list of just one function named `TempMonitorFunction`) and their configurations. Before you can create the function definition, you need the Lambda function ARN. To create the function and its alias, use Lambda's `create-function` and `publish-version` commands. Lambda's `create-function` command requires the ARN of the execution role, even though AWS IoT Greengrass doesn't use that role because permissions are specified in the Greengrass group role. You can use the IAM `create-role` command to create an empty role to get an ARN to use with Lambda's `create-function` or you can use an existing execution role.

```
aws greengrass create-function-definition \
    --name {{MyGreengrassFunctions}} \
    --initial-version "{\"Functions\": [{\"Id\": \"TempMonitorFunction\", \"FunctionArn\": \"arn:aws:lambda:us-west-2:123456789012:function:TempMonitor:GG_TempMonitor\", \"FunctionConfiguration\": {\"Executable\": \"temp_monitor.function_handler\", \"MemorySize\": 16000,\"Timeout\": 5}}]}"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/3b0d0080-87e7-48c6-b182-503ec743a08b",
    "CreationTimestamp": "2019-06-19T22:24:44.585Z",
    "Id": "3b0d0080-87e7-48c6-b182-503ec743a08b",
    "LastUpdatedTimestamp": "2019-06-19T22:24:44.585Z",
    "LatestVersion": "67f918b9-efb4-40b0-b87c-de8c9faf085b",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/3b0d0080-87e7-48c6-b182-503ec743a08b/versions/67f918b9-efb4-40b0-b87c-de8c9faf085b",
    "Name": "MyGreengrassFunctions"
}
```
For more information, see [How to Configure Local Resource Access Using the AWS Command Line Interface](https://docs.aws.amazon.com/greengrass/latest/developerguide/lra-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateFunctionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition.html) in *AWS CLI Command Reference*.

### `create-group-certificate-authority`
<a name="greengrass_CreateGroupCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `create-group-certificate-authority`.

**AWS CLI**
**To create a certificate authority (CA) for a group**
The following `create-group-certificate-authority` example creates or rotates a CA for the specified group.

```
aws greengrass create-group-certificate-authority \
    --group-id {{"8eaadd72-ce4b-4f15-892a-0cc4f3a343f1"}}
```
Output:

```
{
    "GroupCertificateAuthorityArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/8eaadd72-ce4b-4f15-892a-0cc4f3a343f1/certificateauthorities/d31630d674c4437f6c5dbc0dca56312a902171ce2d086c38e509c8EXAMPLEcc5"
}
```
For more information, see [AWS IoT Greengrass Security](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-sec.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateGroupCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-group-certificate-authority.html) in *AWS CLI Command Reference*.

### `create-group-version`
<a name="greengrass_CreateGroupVersion_cli_2_topic"></a>

The following code example shows how to use `create-group-version`.

**AWS CLI**
**To create a version of a Greengrass group**
The following `create-group-version` example creates a group version and associates it with the specified group. The version references the core, resource, connector, function, and subscription versions that contain the entities to include in this group version. You must create these entities before you can create the group version.
To create a resource definition with an initial version, use the `create-resource-definition` command.To create a connector definition with an initial version, use the `create-connector-definition` command.To create a function definition with an initial version, use the `create-function-definition` command.To create a subscription definition with an initial version, use the `create-subscription-definition` command.To retrieve the ARN of the latest core definition version, use the `get-group-version` command and specify the ID of the latest group version.

```
aws greengrass create-group-version \
    --group-id "ce2e7d01-3240-4c24-b8e6-f6f6e7a9eeca" \
    --core-definition-version-arn "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/6a630442-8708-4838-ad36-eb98849d975e/versions/6c87151b-1fb4-4cb2-8b31-6ee715d8f8ba" \
    --resource-definition-version-arn "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38/versions/a5f94d0b-f6bc-40f4-bb78-7a1c5fe13ba1" \
    --connector-definition-version-arn "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/55d0052b-0d7d-44d6-b56f-21867215e118/versions/78a3331b-895d-489b-8823-17b4f9f418a0" \
    --function-definition-version-arn "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/3b0d0080-87e7-48c6-b182-503ec743a08b/versions/67f918b9-efb4-40b0-b87c-de8c9faf085b" \
    --subscription-definition-version-arn "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/9d611d57-5d5d-44bd-a3b4-feccbdd69112/versions/aa645c47-ac90-420d-9091-8c7ffa4f103f"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/ce2e7d01-3240-4c24-b8e6-f6f6e7a9eeca/versions/e10b0459-4345-4a09-88a4-1af1f5d34638",
    "CreationTimestamp": "2019-06-20T18:42:47.020Z",
    "Id": "ce2e7d01-3240-4c24-b8e6-f6f6e7a9eeca",
    "Version": "e10b0459-4345-4a09-88a4-1af1f5d34638"
}
```
For more information, see [Overview of the AWS IoT Greengrass Group Object Model](https://docs.aws.amazon.com/greengrass/latest/developerguide/deployments.html#api-overview) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateGroupVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-group-version.html) in *AWS CLI Command Reference*.

### `create-group`
<a name="greengrass_CreateGroup_cli_2_topic"></a>

The following code example shows how to use `create-group`.

**AWS CLI**
**To create a Greeengrass group**
The following `create-group` example creates a group named `cli-created-group`.

```
aws greengrass create-group \
    --name {{cli-created-group}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/4e22bd92-898c-436b-ade5-434d883ff749",
    "CreationTimestamp": "2019-06-25T18:07:17.688Z",
    "Id": "4e22bd92-898c-436b-ade5-434d883ff749",
    "LastUpdatedTimestamp": "2019-06-25T18:07:17.688Z",
    "Name": "cli-created-group"
}
```
For more information, see [Overview of the AWS IoT Greengrass Group Object Model](https://docs.aws.amazon.com/greengrass/latest/developerguide/deployments.html#api-overview) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-group.html) in *AWS CLI Command Reference*.

### `create-logger-definition-version`
<a name="greengrass_CreateLoggerDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-logger-definition-version`.

**AWS CLI**
**To create a logger definition version**
The following `create-logger-definition-version` example creates a logger definition version and associates it with a logger definition. The version defines four logging configurations: 1) system component logs on the file system of the core device, 2) user-defined Lambda function logs on the file system of the core device, 3) system component logs in Amazon CloudWatch Logs, and 4) user-defined Lambda function logs in Amazon CloudWatch Logs. Note: For CloudWatch Logs integration, your group role must grant appropriate permissions.

```
aws greengrass create-logger-definition-version \
    --logger-definition-id {{"a454b62a-5d56-4ca9-bdc4-8254e1662cb0"}} \
    --loggers "[{\"Id\":\"1\",\"Component\":\"GreengrassSystem\",\"Level\":\"ERROR\",\"Space\":10240,\"Type\":\"FileSystem\"},{\"Id\":\"2\",\"Component\":\"Lambda\",\"Level\":\"INFO\",\"Space\":10240,\"Type\":\"FileSystem\"},{\"Id\":\"3\",\"Component\":\"GreengrassSystem\",\"Level\":\"WARN\",\"Type\":\"AWSCloudWatch\"},{\"Id\":\"4\",\"Component\":\"Lambda\",\"Level\":\"INFO\",\"Type\":\"AWSCloudWatch\"}]"
```
Output:

```
{
 "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/a454b62a-5d56-4ca9-bdc4-8254e1662cb0/versions/49aedb1e-01a3-4d39-9871-3a052573f1ea",
 "Version": "49aedb1e-01a3-4d39-9871-3a052573f1ea",
 "CreationTimestamp": "2019-07-24T00:04:48.523Z",
 "Id": "a454b62a-5d56-4ca9-bdc4-8254e1662cb0"
}
```
For more information, see [Monitoring with AWS IoT Greengrass Logs](https://docs.aws.amazon.com/greengrass/latest/developerguide/greengrass-logs-overview.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateLoggerDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-logger-definition-version.html) in *AWS CLI Command Reference*.

### `create-logger-definition`
<a name="greengrass_CreateLoggerDefinition_cli_2_topic"></a>

The following code example shows how to use `create-logger-definition`.

**AWS CLI**
**To create a logger definition**
The following `create-logger-definition` example creates a logger definition that contains an initial logger definition version. The initial version defines three logging configurations: 1) system component logs on the file system of the core device, 2) user-defined Lambda function logs on the file system of the core device, and 3) user-defined Lambda function logs in Amazon CloudWatch Logs. Note: For CloudWatch Logs integration, your group role must grant appropriate permissions.

```
aws greengrass create-logger-definition \
    --name {{"LoggingConfigs"}} \
    --initial-version "{\"Loggers\":[{\"Id\":\"1\",\"Component\":\"GreengrassSystem\",\"Level\":\"ERROR\",\"Space\":10240,\"Type\":\"FileSystem\"},{\"Id\":\"2\",\"Component\":\"Lambda\",\"Level\":\"INFO\",\"Space\":10240,\"Type\":\"FileSystem\"},{\"Id\":\"3\",\"Component\":\"Lambda\",\"Level\":\"INFO\",\"Type\":\"AWSCloudWatch\"}]}"
```
Output:

```
{
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/a454b62a-5d56-4ca9-bdc4-8254e1662cb0/versions/de1d9854-1588-4525-b25e-b378f60f2322",
    "Name": "LoggingConfigs",
    "LastUpdatedTimestamp": "2019-07-23T23:52:17.165Z",
    "LatestVersion": "de1d9854-1588-4525-b25e-b378f60f2322",
    "CreationTimestamp": "2019-07-23T23:52:17.165Z",
    "Id": "a454b62a-5d56-4ca9-bdc4-8254e1662cb0",
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/a454b62a-5d56-4ca9-bdc4-8254e1662cb0"
}
```
For more information, see [Monitoring with AWS IoT Greengrass Logs](https://docs.aws.amazon.com/greengrass/latest/developerguide/greengrass-logs-overview.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateLoggerDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-logger-definition.html) in *AWS CLI Command Reference*.

### `create-resource-definition-version`
<a name="greengrass_CreateResourceDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-resource-definition-version`.

**AWS CLI**
**To create a version of a resource definition**
The following `create-resource-definition-version` example creates a new version of a TwilioAuthToken.

```
aws greengrass create-resource-definition-version \
    --resource-definition-id {{"c8bb9ebc-c3fd-40a4-9c6a-568d75569d38"}} \
    --resources "[{\"Id\": \"TwilioAuthToken\",\"Name\": \"MyTwilioAuthToken\",\"ResourceDataContainer\": {\"SecretsManagerSecretResourceData\": {\"ARN\": \"arn:aws:secretsmanager:us-west-2:123456789012:secret:greengrass-TwilioAuthToken-ntSlp6\"}}}]"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38/versions/b3bcada0-5fb6-42df-bf0b-1ee4f15e769e",
    "CreationTimestamp": "2019-06-24T21:17:25.623Z",
    "Id": "c8bb9ebc-c3fd-40a4-9c6a-568d75569d38",
    "Version": "b3bcada0-5fb6-42df-bf0b-1ee4f15e769e"
}
```
+  For API details, see [CreateResourceDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition-version.html) in *AWS CLI Command Reference*.

### `create-resource-definition`
<a name="greengrass_CreateResourceDefinition_cli_2_topic"></a>

The following code example shows how to use `create-resource-definition`.

**AWS CLI**
**To create a resource definition**
The following `create-resource-definition` example creates a resource definition that contains a list of resources to be used in a Greengrass group. In this example, an initial version of the resource definition is included by providing a list of resources. The list includes one resource for a Twilio authorization token and the ARN for a secret stored in AWS Secrets Manager. You must create the secret before you can create the resource definition.

```
aws greengrass create-resource-definition \
    --name {{MyGreengrassResources}} \
    --initial-version "{\"Resources\": [{\"Id\": \"TwilioAuthToken\",\"Name\": \"MyTwilioAuthToken\",\"ResourceDataContainer\": {\"SecretsManagerSecretResourceData\": {\"ARN\": \"arn:aws:secretsmanager:us-west-2:123456789012:secret:greengrass-TwilioAuthToken-ntSlp6\"}}}]}"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38",
    "CreationTimestamp": "2019-06-19T21:51:28.212Z",
    "Id": "c8bb9ebc-c3fd-40a4-9c6a-568d75569d38",
    "LastUpdatedTimestamp": "2019-06-19T21:51:28.212Z",
    "LatestVersion": "a5f94d0b-f6bc-40f4-bb78-7a1c5fe13ba1",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38/versions/a5f94d0b-f6bc-40f4-bb78-7a1c5fe13ba1",
    "Name": "MyGreengrassResources"
}
```
For more information, see [How to Configure Local Resource Access Using the AWS Command Line Interface](https://docs.aws.amazon.com/greengrass/latest/developerguide/lra-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateResourceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition.html) in *AWS CLI Command Reference*.

### `create-software-update-job`
<a name="greengrass_CreateSoftwareUpdateJob_cli_2_topic"></a>

The following code example shows how to use `create-software-update-job`.

**AWS CLI**
**To create a software update job for a core**
The following `create-software-update-job` example creates an over-the-air (OTA) update job to update the AWS IoT Greengrass Core software on the core whose name is `MyFirstGroup_Core`. This command requires an IAM role that allows access to software update packages in Amazon S3 and includes `iot.amazonaws.com` as a trusted entity.

```
aws greengrass create-software-update-job \
    --update-targets-architecture {{armv7l}} \
    --update-targets [\"arn:aws:iot:us-west-2:123456789012:thing/MyFirstGroup_Core\"] \
    --update-targets-operating-system {{raspbian}} \
    --software-to-update {{core}} \
    --s3-url-signer-role {{arn:aws:iam::123456789012:role/OTA_signer_role}} \
    --update-agent-log-level {{WARN}}
```
Output:

```
{
    "IotJobId": "GreengrassUpdateJob_30b353e3-3af7-4786-be25-4c446663c09e",
    "IotJobArn": "arn:aws:iot:us-west-2:123456789012:job/GreengrassUpdateJob_30b353e3-3af7-4786-be25-4c446663c09e",
    "PlatformSoftwareVersion": "1.9.3"
}
```
For more information, see [OTA Updates of AWS IoT Greengrass Core Software](https://docs.aws.amazon.com/greengrass/latest/developerguide/core-ota-update.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateSoftwareUpdateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-software-update-job.html) in *AWS CLI Command Reference*.

### `create-subscription-definition-version`
<a name="greengrass_CreateSubscriptionDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `create-subscription-definition-version`.

**AWS CLI**
**To create a new version of a subscription definition**
The following `create-subscription-definition-version` example creates a new version of a subscription definition that contains three subscriptions: a trigger notification, a temperature input, and an output status.

```
aws greengrass create-subscription-definition-version \
    --subscription-definition-id {{"9d611d57-5d5d-44bd-a3b4-feccbdd69112"}} \
    --subscriptions "[{\"Id\": \"TriggerNotification\", \"Source\": \"arn:aws:lambda:us-west-2:123456789012:function:TempMonitor:GG_TempMonitor\", \"Subject\": \"twilio/txt\", \"Target\": \"arn:aws:greengrass:us-west-2::/connectors/TwilioNotifications/versions/1\"},{\"Id\": \"TemperatureInput\", \"Source\": \"cloud\", \"Subject\": \"temperature/input\", \"Target\": \"arn:aws:lambda:us-west-2:123456789012:function:TempMonitor:GG_TempMonitor\"},{\"Id\": \"OutputStatus\", \"Source\": \"arn:aws:greengrass:us-west-2::/connectors/TwilioNotifications/versions/1\", \"Subject\": \"twilio/message/status\", \"Target\": \"cloud\"}]"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/9d611d57-5d5d-44bd-a3b4-feccbdd69112/versions/7b65dfae-50b6-4d0f-b3e0-27728bfb0620",
    "CreationTimestamp": "2019-06-24T21:21:33.837Z",
    "Id": "9d611d57-5d5d-44bd-a3b4-feccbdd69112",
    "Version": "7b65dfae-50b6-4d0f-b3e0-27728bfb0620"
}
```
+  For API details, see [CreateSubscriptionDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-subscription-definition-version.html) in *AWS CLI Command Reference*.

### `create-subscription-definition`
<a name="greengrass_CreateSubscriptionDefinition_cli_2_topic"></a>

The following code example shows how to use `create-subscription-definition`.

**AWS CLI**
**To create a subscription definition**
The following `create-subscription-definition` example creates a subscription definition and specifies its initial version. The initial version contains three subscriptions: one for the MQTT topic to which the connector subscribes, one to allow a function to receive temperature readings from AWS IoT, and one to allow AWS IoT to receive status information from the connector. The example provides the ARN for the Lambda function alias that was created earlier by using Lambda's `create-alias` command.

```
aws greengrass create-subscription-definition \
    --initial-version "{\"Subscriptions\": [{\"Id\": \"TriggerNotification\", \"Source\": \"arn:aws:lambda:us-west-2:123456789012:function:TempMonitor:GG_TempMonitor\", \"Subject\": \"twilio/txt\", \"Target\": \"arn:aws:greengrass:us-west-2::/connectors/TwilioNotifications/versions/1\"},{\"Id\": \"TemperatureInput\", \"Source\": \"cloud\", \"Subject\": \"temperature/input\", \"Target\": \"arn:aws:lambda:us-west-2:123456789012:function:TempMonitor:GG_TempMonitor\"},{\"Id\": \"OutputStatus\", \"Source\": \"arn:aws:greengrass:us-west-2::/connectors/TwilioNotifications/versions/1\", \"Subject\": \"twilio/message/status\", \"Target\": \"cloud\"}]}"
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/9d611d57-5d5d-44bd-a3b4-feccbdd69112",
    "CreationTimestamp": "2019-06-19T22:34:26.677Z",
    "Id": "9d611d57-5d5d-44bd-a3b4-feccbdd69112",
    "LastUpdatedTimestamp": "2019-06-19T22:34:26.677Z",
    "LatestVersion": "aa645c47-ac90-420d-9091-8c7ffa4f103f",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/9d611d57-5d5d-44bd-a3b4-feccbdd69112/versions/aa645c47-ac90-420d-9091-8c7ffa4f103f"
}
```
For more information, see [Getting Started with Connectors (CLI)](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [CreateSubscriptionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-subscription-definition.html) in *AWS CLI Command Reference*.

### `delete-connector-definition`
<a name="greengrass_DeleteConnectorDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-connector-definition`.

**AWS CLI**
**To delete a connector definition**
The following `delete-connector-definition` example deletes the specified Greengrass connector definition. If you delete a connector definition that is used by a group, that group can't be deployed successfully.

```
aws greengrass delete-connector-definition \
    --connector-definition-id {{"b5c4ebfd-f672-49a3-83cd-31c7216a7bb8"}}
```
This command produces no output.
+  For API details, see [DeleteConnectorDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-connector-definition.html) in *AWS CLI Command Reference*.

### `delete-core-definition`
<a name="greengrass_DeleteCoreDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-core-definition`.

**AWS CLI**
**To delete a core definition**
The following `delete-core-definition` example deletes the specified Greengrass core definition, including all versions. If you delete a core that is associated with a Greengrass group, that group can't be deployed successfully.

```
aws greengrass delete-core-definition \
    --core-definition-id {{"ff36cc5f-9f98-4994-b468-9d9b6dc52abd"}}
```
This command produces no output.
+  For API details, see [DeleteCoreDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-core-definition.html) in *AWS CLI Command Reference*.

### `delete-device-definition`
<a name="greengrass_DeleteDeviceDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-device-definition`.

**AWS CLI**
**To delete a device definition**
The following `delete-device-definition` example deletes the specified device definition, including all of its versions. If you delete a device definition version that is used by a group version, the group version cannot be deployed successfully.

```
aws greengrass delete-device-definition \
    --device-definition-id {{"f9ba083d-5ad4-4534-9f86-026a45df1ccd"}}
```
This command produces no output.
+  For API details, see [DeleteDeviceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-device-definition.html) in *AWS CLI Command Reference*.

### `delete-function-definition`
<a name="greengrass_DeleteFunctionDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-function-definition`.

**AWS CLI**
**To delete a function definition**
The following `delete-function-definition` example deletes the specified Greengrass function definition. If you delete a function definition that is used by a group, that group can't be deployed successfully.

```
aws greengrass delete-function-definition \
    --function-definition-id {{"fd4b906a-dff3-4c1b-96eb-52ebfcfac06a"}}
```
This command produces no output.
+  For API details, see [DeleteFunctionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-function-definition.html) in *AWS CLI Command Reference*.

### `delete-group`
<a name="greengrass_DeleteGroup_cli_2_topic"></a>

The following code example shows how to use `delete-group`.

**AWS CLI**
**To delete a group**
The following `delete-group` example deletes the specified Greengrass group.

```
aws greengrass delete-group \
    --group-id {{"4e22bd92-898c-436b-ade5-434d883ff749"}}
```
This command produces no output.
+  For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-group.html) in *AWS CLI Command Reference*.

### `delete-logger-definition`
<a name="greengrass_DeleteLoggerDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-logger-definition`.

**AWS CLI**
**To delete a logger definition**
The following `delete-logger-definition` example deletes the specified logger definition, including all logger definition versions. If you delete a logger definition version that is used by a group version, the group version cannot be deployed successfully.

```
aws greengrass delete-logger-definition \
    --logger-definition-id {{"a454b62a-5d56-4ca9-bdc4-8254e1662cb0"}}
```
This command produces no output.
For more information, see [Monitoring with AWS IoT Greengrass Logs](https://docs.aws.amazon.com/greengrass/latest/developerguide/greengrass-logs-overview.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [DeleteLoggerDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-logger-definition.html) in *AWS CLI Command Reference*.

### `delete-resource-definition`
<a name="greengrass_DeleteResourceDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-resource-definition`.

**AWS CLI**
**To delete a resource definition**
The following `delete-resource-definition` example deletes the specified resource definition, including all resource versions. If you delete a resource definition that is used by a group, that group can't be deployed successfully.

```
aws greengrass delete-resource-definition \
    --resource-definition-id {{"ad8c101d-8109-4b0e-b97d-9cc5802ab658"}}
```
This command produces no output.
+  For API details, see [DeleteResourceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-resource-definition.html) in *AWS CLI Command Reference*.

### `delete-subscription-definition`
<a name="greengrass_DeleteSubscriptionDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-subscription-definition`.

**AWS CLI**
**To delete a subscription definition**
The following `delete-subscription-definition` example deletes the specified Greengrass subscription definition. If you delete a subscription that is being used by a group, that group can't be deployed successfully.

```
aws greengrass delete-subscription-definition \
    --subscription-definition-id {{"cd6f1c37-d9a4-4e90-be94-01a7404f5967"}}
```
This command produces no output.
+  For API details, see [DeleteSubscriptionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-subscription-definition.html) in *AWS CLI Command Reference*.

### `disassociate-role-from-group`
<a name="greengrass_DisassociateRoleFromGroup_cli_2_topic"></a>

The following code example shows how to use `disassociate-role-from-group`.

**AWS CLI**
**To disassociate the role from a Greengrass group**
The following `disassociate-role-from-group` example disassociates the IAM role from the specified Greengrass group.

```
aws greengrass disassociate-role-from-group \
    --group-id {{2494ee3f-7f8a-4e92-a78b-d205f808b84b}}
```
Output:

```
{
    "DisassociatedAt": "2019-09-10T20:05:49Z"
}
```
For more information, see [Configure the Group Role](https://docs.aws.amazon.com/greengrass/latest/developerguide/config-iam-roles.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [DisassociateRoleFromGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/disassociate-role-from-group.html) in *AWS CLI Command Reference*.

### `disassociate-service-role-from-account`
<a name="greengrass_DisassociateServiceRoleFromAccount_cli_2_topic"></a>

The following code example shows how to use `disassociate-service-role-from-account`.

**AWS CLI**
**To disassociate a service role from your AWS account**
The following `disassociate-service-role-from-account` example removes the service role that is associated with your AWS account. If you are not using the service role in any AWS Region, use the `delete-role-policy` command to detach the `AWSGreengrassResourceAccessRolePolicy` managed policy from the role, and then use the `delete-role` command to delete the role.

```
aws greengrass disassociate-service-role-from-account
```
Output:

```
{
    "DisassociatedAt": "2019-06-25T22:12:55Z"
}
```
For more information, see [Greengrass Service Role](https://docs.aws.amazon.com/greengrass/latest/developerguide/service-role.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [DisassociateServiceRoleFromAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/disassociate-service-role-from-account.html) in *AWS CLI Command Reference*.

### `get-associated-role`
<a name="greengrass_GetAssociatedRole_cli_2_topic"></a>

The following code example shows how to use `get-associated-role`.

**AWS CLI**
**To get the role associated with a Greengrass group**
The following `get-associated-role` example gets the IAM role that's associated with the specified Greengrass group. The group role is used by local Lambda functions and connectors to access AWS services.

```
aws greengrass get-associated-role \
    --group-id {{2494ee3f-7f8a-4e92-a78b-d205f808b84b}}
```
Output:

```
{
    "RoleArn": "arn:aws:iam::123456789012:role/GG-Group-Role",
    "AssociatedAt": "2019-09-10T20:03:30Z"
}
```
For more information, see [Configure the Group Role](https://docs.aws.amazon.com/greengrass/latest/developerguide/config-iam-roles.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [GetAssociatedRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-associated-role.html) in *AWS CLI Command Reference*.

### `get-bulk-deployment-status`
<a name="greengrass_GetBulkDeploymentStatus_cli_2_topic"></a>

The following code example shows how to use `get-bulk-deployment-status`.

**AWS CLI**
**To check the status of your bulk deployment**
The following `get-bulk-deployment-status` example retrieves status information for the specified bulk deployment operation. In this example, the file that specified the groups to be deployed has an invalid input record.

```
aws greengrass get-bulk-deployment-status \
    --bulk-deployment-id {{"870fb41b-6288-4e0c-bc76-a7ba4b4d3267"}}
```
Output:

```
{
    "BulkDeploymentMetrics": {
        "InvalidInputRecords": 1,
        "RecordsProcessed": 1,
        "RetryAttempts": 0
    },
    "BulkDeploymentStatus": "Completed",
    "CreatedAt": "2019-06-25T16:11:33.265Z",
    "tags": {}
}
```
For more information, see [Create Bulk Deployments for Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [GetBulkDeploymentStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-bulk-deployment-status.html) in *AWS CLI Command Reference*.

### `get-connectivity-info`
<a name="greengrass_GetConnectivityInfo_cli_2_topic"></a>

The following code example shows how to use `get-connectivity-info`.

**AWS CLI**
**To get the connectivity information for a Greengrass core**
The following `get-connectivity-info` example displays the endpoints that devices can use to connect to the specified Greengrass core. Connectivity information is a list of IP addresses or domain names, with corresponding port numbers and optional customer-defined metadata.

```
aws greengrass get-connectivity-info \
    --thing-name {{"MyGroup_Core"}}
```
Output:

```
{
    "ConnectivityInfo": [
        {
            "Metadata": "",
            "PortNumber": 8883,
            "HostAddress": "127.0.0.1",
            "Id": "AUTOIP_127.0.0.1_0"
        },
        {
            "Metadata": "",
            "PortNumber": 8883,
            "HostAddress": "192.168.1.3",
            "Id": "AUTOIP_192.168.1.3_1"
        },
        {
            "Metadata": "",
            "PortNumber": 8883,
            "HostAddress": "::1",
            "Id": "AUTOIP_::1_2"
        },
        {
            "Metadata": "",
            "PortNumber": 8883,
            "HostAddress": "fe80::1e69:ed93:f5b:f6d",
            "Id": "AUTOIP_fe80::1e69:ed93:f5b:f6d_3"
        }
    ]
}
```
+  For API details, see [GetConnectivityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connectivity-info.html) in *AWS CLI Command Reference*.

### `get-connector-definition-version`
<a name="greengrass_GetConnectorDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-connector-definition-version`.

**AWS CLI**
**To retrieve information about a specific version of a connector definition**
The following `get-connector-definition-version` example retrieves information about the specified version of the specified connector definition. To retrieve the IDs of all versions of the connector definition, use the `list-connector-definition-versions` command. To retrieve the ID of the last version added to the connector definition, use the `get-connector-definition` command and check the `LatestVersion` property.

```
aws greengrass get-connector-definition-version \
    --connector-definition-id {{"b5c4ebfd-f672-49a3-83cd-31c7216a7bb8"}} \
    --connector-definition-version-id {{"63c57963-c7c2-4a26-a7e2-7bf478ea2623"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8/versions/63c57963-c7c2-4a26-a7e2-7bf478ea2623",
    "CreationTimestamp": "2019-06-19T19:30:01.300Z",
    "Definition": {
        "Connectors": [
            {
                "ConnectorArn": "arn:aws:greengrass:us-west-2::/connectors/SNS/versions/1",
                "Id": "MySNSConnector",
                "Parameters": {
                    "DefaultSNSArn": "arn:aws:sns:us-west-2:123456789012:GGConnectorTopic"
                }
            }
        ]
    },
    "Id": "b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
    "Version": "63c57963-c7c2-4a26-a7e2-7bf478ea2623"
}
```
For more information, see [Integrate with Services and Protocols Using Greengrass Connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [GetConnectorDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition-version.html) in *AWS CLI Command Reference*.

### `get-connector-definition`
<a name="greengrass_GetConnectorDefinition_cli_2_topic"></a>

The following code example shows how to use `get-connector-definition`.

**AWS CLI**
**To retrieve information about a connector definition**
The following `get-connector-definition` example retrieves information about the specified connector definition. To retrieve the IDs of your connector definitions, use the `list-connector-definitions` command.

```
aws greengrass get-connector-definition \
    --connector-definition-id {{"b5c4ebfd-f672-49a3-83cd-31c7216a7bb8"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
    "CreationTimestamp": "2019-06-19T19:30:01.300Z",
    "Id": "b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
    "LastUpdatedTimestamp": "2019-06-19T19:30:01.300Z",
    "LatestVersion": "63c57963-c7c2-4a26-a7e2-7bf478ea2623",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8/versions/63c57963-c7c2-4a26-a7e2-7bf478ea2623",
    "Name": "MySNSConnector",
    "tags": {}
}
```
For more information, see [Integrate with Services and Protocols Using Greengrass Connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [GetConnectorDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition.html) in *AWS CLI Command Reference*.

### `get-core-definition-version`
<a name="greengrass_GetCoreDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-core-definition-version`.

**AWS CLI**
**To retrieve details about a specific version of the Greengrass core definition**
The following `get-core-definition-version` example retrieves information about the specified version of the specified core definition. To retrieve the IDs of all versions of the core definition, use the `list-core-definition-versions` command. To retrieve the ID of the last version added to the core definition, use the `get-core-definition` command and check the `LatestVersion` property.

```
aws greengrass get-core-definition-version \
    --core-definition-id {{"c906ed39-a1e3-4822-a981-7b9bd57b4b46"}}  \
    --core-definition-version-id {{"42aeeac3-fd9d-4312-a8fd-ffa9404a20e0"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/c906ed39-a1e3-4822-a981-7b9bd57b4b46/versions/42aeeac3-fd9d-4312-a8fd-ffa9404a20e0",
    "CreationTimestamp": "2019-06-18T16:21:21.351Z",
    "Definition": {
        "Cores": [
            {
                "CertificateArn": "arn:aws:iot:us-west-2:123456789012:cert/928dea7b82331b47c3ff77b0e763fc5e64e2f7c884e6ef391baed9b6b8e21b45",
                "Id": "1a39aac7-0885-4417-91f6-23e4cea6c511",
                "SyncShadow": false,
                "ThingArn": "arn:aws:iot:us-west-2:123456789012:thing/GGGroup4Pi3_Core"
            }
        ]
    },
    "Id": "c906ed39-a1e3-4822-a981-7b9bd57b4b46",
    "Version": "42aeeac3-fd9d-4312-a8fd-ffa9404a20e0"
}
```
+  For API details, see [GetCoreDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-core-definition-version.html) in *AWS CLI Command Reference*.

### `get-core-definition`
<a name="greengrass_GetCoreDefinition_cli_2_topic"></a>

The following code example shows how to use `get-core-definition`.

**AWS CLI**
**To retrieve details for a Greengrass core definition**
The following `get-core-definition` example retrieves information about the specified core definition. To retrieve the IDs of your core definitions, use the `list-core-definitions` command.

```
aws greengrass get-core-definition \
    --core-definition-id {{"c906ed39-a1e3-4822-a981-7b9bd57b4b46"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/237d6916-27cf-457f-ba0c-e86cfb5d25cd",
    "CreationTimestamp": "2018-10-18T04:47:06.721Z",
    "Id": "237d6916-27cf-457f-ba0c-e86cfb5d25cd",
    "LastUpdatedTimestamp": "2018-10-18T04:47:06.721Z",
    "LatestVersion": "bd2cd6d4-2bc5-468a-8962-39e071e34b68",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/237d6916-27cf-457f-ba0c-e86cfb5d25cd/versions/bd2cd6d4-2bc5-468a-8962-39e071e34b68",
    "tags": {}
}
```
+  For API details, see [GetCoreDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-core-definition.html) in *AWS CLI Command Reference*.

### `get-deployment-status`
<a name="greengrass_GetDeploymentStatus_cli_2_topic"></a>

The following code example shows how to use `get-deployment-status`.

**AWS CLI**
**To retrieve the status of a deployment**
The following `get-deployment-status` example retrieves the status for the specified deployment of the specified Greengrass group. To get the deployment ID, use the `list-deployments` command and specify the group ID.

```
aws greengrass get-deployment-status \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}} \
    --deployment-id {{"1065b8a0-812b-4f21-9d5d-e89b232a530f"}}
```
Output:

```
{
    "DeploymentStatus": "Success",
    "DeploymentType": "NewDeployment",
    "UpdatedAt": "2019-06-18T17:04:44.761Z"
}
```
+  For API details, see [GetDeploymentStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-deployment-status.html) in *AWS CLI Command Reference*.

### `get-device-definition-version`
<a name="greengrass_GetDeviceDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-device-definition-version`.

**AWS CLI**
**To get a device definition version**
The following `get-device-definition-version` example retrieves information about the specified version of the specified device definition. To retrieve the IDs of all versions of the device definition, use the `list-device-definition-versions` command. To retrieve the ID of the last version added to the device definition, use the `get-device-definition` command and check the `LatestVersion` property.

```
aws greengrass get-device-definition-version \
    --device-definition-id {{"f9ba083d-5ad4-4534-9f86-026a45df1ccd"}} \
    --device-definition-version-id {{"83c13984-6fed-447e-84d5-5b8aa45d5f71"}}
```
Output:

```
{
    "Definition": {
        "Devices": [
            {
                "CertificateArn": "arn:aws:iot:us-west-2:123456789012:cert/6c52ce1b47bde88a637e9ccdd45fe4e4c2c0a75a6866f8f63d980ee22fa51e02",
                "ThingArn": "arn:aws:iot:us-west-2:123456789012:thing/ExteriorTherm",
                "SyncShadow": true,
                "Id": "ExteriorTherm"
            },
            {
                "CertificateArn": "arn:aws:iot:us-west-2:123456789012:cert/66a415ec415668c2349a76170b64ac0878231c1e21ec83c10e92a18bd568eb92",
                "ThingArn": "arn:aws:iot:us-west-2:123456789012:thing/InteriorTherm",
                "SyncShadow": true,
                "Id": "InteriorTherm"
            }
        ]
    },
    "Version": "83c13984-6fed-447e-84d5-5b8aa45d5f71",
    "CreationTimestamp": "2019-09-11T00:15:09.838Z",
    "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd",
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/83c13984-6fed-447e-84d5-5b8aa45d5f71"
}
```
+  For API details, see [GetDeviceDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-device-definition-version.html) in *AWS CLI Command Reference*.

### `get-device-definition`
<a name="greengrass_GetDeviceDefinition_cli_2_topic"></a>

The following code example shows how to use `get-device-definition`.

**AWS CLI**
**To get a device definition**
The following `get-device-definition` example retrieves information about the specified device definition. To retrieve the IDs of your device definitions, use the `list-device-definitions` command.

```
aws greengrass get-device-definition \
    --device-definition-id {{"f9ba083d-5ad4-4534-9f86-026a45df1ccd"}}
```
Output:

```
{
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/83c13984-6fed-447e-84d5-5b8aa45d5f71",
    "Name": "TemperatureSensors",
    "tags": {},
    "LastUpdatedTimestamp": "2019-09-11T00:19:03.698Z",
    "LatestVersion": "83c13984-6fed-447e-84d5-5b8aa45d5f71",
    "CreationTimestamp": "2019-09-11T00:11:06.197Z",
    "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd",
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd"
}
```
+  For API details, see [GetDeviceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-device-definition.html) in *AWS CLI Command Reference*.

### `get-function-definition-version`
<a name="greengrass_GetFunctionDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-function-definition-version`.

**AWS CLI**
**To retrieve details about a specific version of a Lambda function**
The following `get-function-definition-version` retrieves information about the specified version of the specified function definition. To retrieve the IDs of all versions of the function definition, use the `list-function-definition-versions` command. To retrieve the ID of the last version added to the function definition, use the `get-function-definition` command and check the `LatestVersion` property.

```
aws greengrass get-function-definition-version \
    --function-definition-id {{"063f5d1a-1dd1-40b4-9b51-56f8993d0f85"}} \
    --function-definition-version-id {{"9748fda7-1589-4fcc-ac94-f5559e88678b"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/9748fda7-1589-4fcc-ac94-f5559e88678b",
    "CreationTimestamp": "2019-06-18T17:04:30.776Z",
    "Definition": {
        "Functions": [
            {
                "FunctionArn": "arn:aws:lambda:::function:GGIPDetector:1",
                "FunctionConfiguration": {
                    "Environment": {},
                    "MemorySize": 32768,
                    "Pinned": true,
                    "Timeout": 3
                },
                "Id": "26b69bdb-e547-46bc-9812-84ec04b6cc8c"
            },
            {
                "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:Greengrass_HelloWorld:GG_HelloWorld",
                "FunctionConfiguration": {
                    "EncodingType": "json",
                    "Environment": {
                        "Variables": {}
                    },
                    "MemorySize": 16384,
                    "Pinned": true,
                    "Timeout": 25
                },
                "Id": "384465a8-eedf-48c6-b793-4c35f7bfae9b"
            }
        ]
    },
    "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
    "Version": "9748fda7-1589-4fcc-ac94-f5559e88678b"
}
```
+  For API details, see [GetFunctionDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-function-definition-version.html) in *AWS CLI Command Reference*.

### `get-function-definition`
<a name="greengrass_GetFunctionDefinition_cli_2_topic"></a>

The following code example shows how to use `get-function-definition`.

**AWS CLI**
**To retrieve a function definition**
The following `get-function-definition` example displays details for the specified function definition. To retrieve the IDs of your function definitions, use the `list-function-definitions` command.

```
aws greengrass get-function-definition \
    --function-definition-id {{"063f5d1a-1dd1-40b4-9b51-56f8993d0f85"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
    "CreationTimestamp": "2019-06-18T16:21:21.431Z",
    "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
    "LastUpdatedTimestamp": "2019-06-18T16:21:21.431Z",
    "LatestVersion": "9748fda7-1589-4fcc-ac94-f5559e88678b",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/9748fda7-1589-4fcc-ac94-f5559e88678b",
    "tags": {}
}
```
+  For API details, see [GetFunctionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-function-definition.html) in *AWS CLI Command Reference*.

### `get-group-certificate-authority`
<a name="greengrass_GetGroupCertificateAuthority_cli_2_topic"></a>

The following code example shows how to use `get-group-certificate-authority`.

**AWS CLI**
**To retrieve the CA associated with a Greengrass group**
The following `get-group-certificate-authority` example retrieves the certificate authority (CA) that is associated with the specified Greengrass group. To get the certificate authority ID, use the `list-group-certificate-authorities` command and specify the group ID.

```
aws greengrass get-group-certificate-authority \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}} \
    --certificate-authority-id {{"f0430e1736ea8ed30cc5d5de9af67a7e3586bad9ae4d89c2a44163f65fdd8cf6"}}
```
Output:

```
{
    "GroupCertificateAuthorityArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/certificateauthorities/f0430e1736ea8ed30cc5d5de9af67a7e3586bad9ae4d89c2a44163f65fdd8cf6",
    "GroupCertificateAuthorityId": "f0430e1736ea8ed30cc5d5de9af67a7e3586bad9ae4d89c2a44163f65fdd8cf6",
    "PemEncodedCertificate": "-----BEGIN CERTIFICATE-----
MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBWEXAMPLEGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDEXAMPLEEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAEXAMPLESBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jEXAMPLENMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0EXAMPLEBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWEXAMPLEDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWEXAMPLEgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5EXAMPLE8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CEXAMPLE93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswYEXAMPLEgpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKEXAMPLEAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=
-----END CERTIFICATE-----\n"
}
```
+  For API details, see [GetGroupCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-group-certificate-authority.html) in *AWS CLI Command Reference*.

### `get-group-certificate-configuration`
<a name="greengrass_GetGroupCertificateConfiguration_cli_2_topic"></a>

The following code example shows how to use `get-group-certificate-configuration`.

**AWS CLI**
**To retrieve the configuration for the certificate authority used by the Greengrass group**
The following `get-group-certificate-configuration` example retrieves the configuration for the certificate authority (CA) used by the specified Greengrass group.

```
aws greengrass get-group-certificate-configuration \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}}
```
Output:

```
{
    "CertificateAuthorityExpiryInMilliseconds": 2524607999000,
    "CertificateExpiryInMilliseconds": 604800000,
    "GroupId": "1013db12-8b58-45ff-acc7-704248f66731"
}
```
+  For API details, see [GetGroupCertificateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-group-certificate-configuration.html) in *AWS CLI Command Reference*.

### `get-group-version`
<a name="greengrass_GetGroupVersion_cli_2_topic"></a>

The following code example shows how to use `get-group-version`.

**AWS CLI**
**To retrieve information about a version of a Greengrass group**
The following `get-group-version` example retrieves information about the specified version of the specified group. To retrieve the IDs of all versions of the group, use the `list-group-versions` command. To retrieve the ID of the last version added to the group, use the `get-group` command and check the `LatestVersion` property.

```
aws greengrass get-group-version \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}}  \
    --group-version-id {{"115136b3-cfd7-4462-b77f-8741a4b00e5e"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/115136b3-cfd7-4462-b77f-8741a4b00e5e",
    "CreationTimestamp": "2019-06-18T17:04:30.915Z",
    "Definition": {
        "CoreDefinitionVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/c906ed39-a1e3-4822-a981-7b9bd57b4b46/versions/42aeeac3-fd9d-4312-a8fd-ffa9404a20e0",
        "FunctionDefinitionVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/9748fda7-1589-4fcc-ac94-f5559e88678b",
        "SubscriptionDefinitionVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152/versions/88ae8699-12ac-4663-ba3f-4d7f0519140b"
    },
    "Id": "1013db12-8b58-45ff-acc7-704248f66731",
    "Version": "115136b3-cfd7-4462-b77f-8741a4b00e5e"
}
```
+  For API details, see [GetGroupVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-group-version.html) in *AWS CLI Command Reference*.

### `get-group`
<a name="greengrass_GetGroup_cli_2_topic"></a>

The following code example shows how to use `get-group`.

**AWS CLI**
**To retrieve information about a Greengrass group**
The following `get-group` example retrieves information about the specified Greengrass group. To retrieve the IDs of your groups, use the `list-groups` command.

```
aws greengrass get-group \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731",
    "CreationTimestamp": "2019-06-18T16:21:21.457Z",
    "Id": "1013db12-8b58-45ff-acc7-704248f66731",
    "LastUpdatedTimestamp": "2019-06-18T16:21:21.457Z",
    "LatestVersion": "115136b3-cfd7-4462-b77f-8741a4b00e5e",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/115136b3-cfd7-4462-b77f-8741a4b00e5e",
    "Name": "GGGroup4Pi3",
    "tags": {}
}
```
+  For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-group.html) in *AWS CLI Command Reference*.

### `get-logger-definition-version`
<a name="greengrass_GetLoggerDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-logger-definition-version`.

**AWS CLI**
**To retrieve information about a version of a logger definition**
The following `get-logger-definition-version` example retrieves information about the specified version of the specified logger definition. To retrieve the IDs of all versions of the logger definition, use the `list-logger-definition-versions` command. To retrieve the ID of the last version added to the logger definition, use the `get-logger-definition` command and check the `LatestVersion` property.

```
aws greengrass get-logger-definition-version \
    --logger-definition-id {{"49eeeb66-f1d3-4e34-86e3-3617262abf23"}} \
    --logger-definition-version-id {{"5e3f6f64-a565-491e-8de0-3c0d8e0f2073"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23/versions/5e3f6f64-a565-491e-8de0-3c0d8e0f2073",
    "CreationTimestamp": "2019-05-08T16:10:13.866Z",
    "Definition": {
        "Loggers": []
    },
    "Id": "49eeeb66-f1d3-4e34-86e3-3617262abf23",
    "Version": "5e3f6f64-a565-491e-8de0-3c0d8e0f2073"
}
```
+  For API details, see [GetLoggerDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-logger-definition-version.html) in *AWS CLI Command Reference*.

### `get-logger-definition`
<a name="greengrass_GetLoggerDefinition_cli_2_topic"></a>

The following code example shows how to use `get-logger-definition`.

**AWS CLI**
**To retrieve information about a logger definition**
The following `get-logger-definition` example retrieves information about the specified logger definition. To retrieve the IDs of your logger definitions, use the `list-logger-definitions` command.

```
aws greengrass get-logger-definition \
    --logger-definition-id {{"49eeeb66-f1d3-4e34-86e3-3617262abf23"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23",
    "CreationTimestamp": "2019-05-08T16:10:13.809Z",
    "Id": "49eeeb66-f1d3-4e34-86e3-3617262abf23",
    "LastUpdatedTimestamp": "2019-05-08T16:10:13.809Z",
    "LatestVersion": "5e3f6f64-a565-491e-8de0-3c0d8e0f2073",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23/versions/5e3f6f64-a565-491e-8de0-3c0d8e0f2073",
    "tags": {}
}
```
+  For API details, see [GetLoggerDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-logger-definition.html) in *AWS CLI Command Reference*.

### `get-resource-definition-version`
<a name="greengrass_GetResourceDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-resource-definition-version`.

**AWS CLI**
**To retrieve information about a specific version of a resource definition**
The following `get-resource-definition-version` example retrieves information about the specified version of the specified resource definition. To retrieve the IDs of all versions of the resource definition, use the `list-resource-definition-versions` command. To retrieve the ID of the last version added to the resource definition, use the `get-resource-definition` command and check the `LatestVersion` property.

```
aws greengrass get-resource-definition-version \
    --resource-definition-id {{"ad8c101d-8109-4b0e-b97d-9cc5802ab658"}} \
    --resource-definition-version-id {{"26e8829a-491a-464d-9c87-664bf6f6f2be"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658/versions/26e8829a-491a-464d-9c87-664bf6f6f2be",
    "CreationTimestamp": "2019-06-19T16:40:59.392Z",
    "Definition": {
        "Resources": [
            {
                "Id": "26ff3f7b-839a-4217-9fdc-a218308b3963",
                "Name": "usb-port",
                "ResourceDataContainer": {
                    "LocalDeviceResourceData": {
                        "GroupOwnerSetting": {
                            "AutoAddGroupOwner": false
                        },
                        "SourcePath": "/dev/bus/usb"
                    }
                }
            }
        ]
    },
    "Id": "ad8c101d-8109-4b0e-b97d-9cc5802ab658",
    "Version": "26e8829a-491a-464d-9c87-664bf6f6f2be"
}
```
+  For API details, see [GetResourceDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-resource-definition-version.html) in *AWS CLI Command Reference*.

### `get-resource-definition`
<a name="greengrass_GetResourceDefinition_cli_2_topic"></a>

The following code example shows how to use `get-resource-definition`.

**AWS CLI**
**To retrieve information about a resource definition**
The following `get-resource-definition` example retrieves information about the specified resource definition. To retrieve the IDs of your resource definitions, use the `list-resource-definitions` command.

```
aws greengrass get-resource-definition \
    --resource-definition-id {{"ad8c101d-8109-4b0e-b97d-9cc5802ab658"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658",
    "CreationTimestamp": "2019-06-19T16:40:59.261Z",
    "Id": "ad8c101d-8109-4b0e-b97d-9cc5802ab658",
    "LastUpdatedTimestamp": "2019-06-19T16:40:59.261Z",
    "LatestVersion": "26e8829a-491a-464d-9c87-664bf6f6f2be",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658/versions/26e8829a-491a-464d-9c87-664bf6f6f2be",
    "tags": {}
}
```
+  For API details, see [GetResourceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-resource-definition.html) in *AWS CLI Command Reference*.

### `get-service-role-for-account`
<a name="greengrass_GetServiceRoleForAccount_cli_2_topic"></a>

The following code example shows how to use `get-service-role-for-account`.

**AWS CLI**
**To retrieve the details for the service role that is attached to your account**
The following `get-service-role-for-account` example retrieves information about the service role that is attached to your AWS account.

```
aws greengrass get-service-role-for-account
```
Output:

```
{
    "AssociatedAt": "2018-10-18T15:59:20Z",
    "RoleArn": "arn:aws:iam::123456789012:role/service-role/Greengrass_ServiceRole"
}
```
For more information, see [Greengrass Service Role](https://docs.aws.amazon.com/greengrass/latest/developerguide/service-role.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [GetServiceRoleForAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-service-role-for-account.html) in *AWS CLI Command Reference*.

### `get-subscription-definition-version`
<a name="greengrass_GetSubscriptionDefinitionVersion_cli_2_topic"></a>

The following code example shows how to use `get-subscription-definition-version`.

**AWS CLI**
**To retrieve information about a specific version of a subscription definition**
The following `get-subscription-definition-version` example retrieves retrieves information about the specified version of the specified subscription definition. To retrieve the IDs of all versions of the subscription definition, use the `list-subscription-definition-versions` command. To retrieve the ID of the last version added to the subscription definition, use the `get-subscription-definition` command and check the `LatestVersion` property.

```
aws greengrass get-subscription-definition-version \
    --subscription-definition-id {{"70e49321-83d5-45d2-bc09-81f4917ae152"}} \
    --subscription-definition-version-id {{"88ae8699-12ac-4663-ba3f-4d7f0519140b"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152/versions/88ae8699-12ac-4663-ba3f-4d7f0519140b",
    "CreationTimestamp": "2019-06-18T17:03:52.499Z",
    "Definition": {
        "Subscriptions": [
            {
                "Id": "692c4484-d89f-4f64-8edd-1a041a65e5b6",
                "Source": "arn:aws:lambda:us-west-2:123456789012:function:Greengrass_HelloWorld:GG_HelloWorld",
                "Subject": "hello/world",
                "Target": "cloud"
            }
        ]
    },
    "Id": "70e49321-83d5-45d2-bc09-81f4917ae152",
    "Version": "88ae8699-12ac-4663-ba3f-4d7f0519140b"
}
```
+  For API details, see [GetSubscriptionDefinitionVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-subscription-definition-version.html) in *AWS CLI Command Reference*.

### `get-subscription-definition`
<a name="greengrass_GetSubscriptionDefinition_cli_2_topic"></a>

The following code example shows how to use `get-subscription-definition`.

**AWS CLI**
**To retrieve information about a subscription definition**
The following `get-subscription-definition` example retrieves information about the specified subscription definition. To retrieve the IDs of your subscription definitions, use the `list-subscription-definitions` command.

```
aws greengrass get-subscription-definition \
    --subscription-definition-id {{"70e49321-83d5-45d2-bc09-81f4917ae152"}}
```
Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152",
    "CreationTimestamp": "2019-06-18T17:03:52.392Z",
    "Id": "70e49321-83d5-45d2-bc09-81f4917ae152",
    "LastUpdatedTimestamp": "2019-06-18T17:03:52.392Z",
    "LatestVersion": "88ae8699-12ac-4663-ba3f-4d7f0519140b",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152/versions/88ae8699-12ac-4663-ba3f-4d7f0519140b",
    "tags": {}
}
```
+  For API details, see [GetSubscriptionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-subscription-definition.html) in *AWS CLI Command Reference*.

### `get-thing-runtime-configuration`
<a name="greengrass_GetThingRuntimeConfiguration_cli_2_topic"></a>

The following code example shows how to use `get-thing-runtime-configuration`.

**AWS CLI**
**To retrieve the runtime configuration of a Greengrass core**
The following `get-thing-runtime-configuration` example retrieves the runtime configuration of a Greengrass core. Before you can retrieve the runtime configuration, you must use the `update-thing-runtime-configuration` command to create a runtime configuration for the core.

```
aws greengrass get-thing-runtime-configuration \
    --thing-name {{SampleGreengrassCore}}
```
Output:

```
{
    "RuntimeConfiguration": {
        "TelemetryConfiguration": {
            "ConfigurationSyncStatus": "OutOfSync",
            "Telemetry": "On"
        }
    }
}
```
For more information, see [Configuring telemetry settings](https://docs.aws.amazon.com/greengrass/latest/developerguide/telemetry.html#configure-telemetry-settings) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [GetThingRuntimeConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-thing-runtime-configuration.html) in *AWS CLI Command Reference*.

### `list-bulk-deployment-detailed-reports`
<a name="greengrass_ListBulkDeploymentDetailedReports_cli_2_topic"></a>

The following code example shows how to use `list-bulk-deployment-detailed-reports`.

**AWS CLI**
**To list information about individual deployments in a bulk deployment**
The following `list-bulk-deployment-detailed-reports` example displays information about the individual deployments in a bulk deployment operation, including status.

```
aws greengrass list-bulk-deployment-detailed-reports \
    --bulk-deployment-id {{42ce9c42-489b-4ed4-b905-8996aa50ef9d}}
```
Output:

```
{
    "Deployments": [
        {
            "DeploymentType": "NewDeployment",
            "DeploymentStatus": "Success",
            "DeploymentId": "123456789012:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "DeploymentArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333/deployments/123456789012:123456789012:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "GroupArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333/versions/123456789012:a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
            "CreatedAt": "2020-01-21T21:34:16.501Z"
        },
        {
            "DeploymentType": "NewDeployment",
            "DeploymentStatus": "InProgress",
            "DeploymentId": "123456789012:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "DeploymentArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-EXAMPLE55555/deployments/123456789012:123456789012:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "GroupArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-EXAMPLE55555/versions/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
            "CreatedAt": "2020-01-21T21:34:16.486Z"
        },
        ...
    ]
}
```
For more information, see [Create Bulk Deployments for Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [ListBulkDeploymentDetailedReports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-bulk-deployment-detailed-reports.html) in *AWS CLI Command Reference*.

### `list-bulk-deployments`
<a name="greengrass_ListBulkDeployments_cli_2_topic"></a>

The following code example shows how to use `list-bulk-deployments`.

**AWS CLI**
**To list bulk deployments**
The following `list-bulk-deployments` example lists all bulk deployments.

```
aws greengrass list-bulk-deployments
```
Output:

```
{
    "BulkDeployments": [
        {
            "BulkDeploymentArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/bulk/deployments/870fb41b-6288-4e0c-bc76-a7ba4b4d3267",
            "BulkDeploymentId": "870fb41b-6288-4e0c-bc76-a7ba4b4d3267",
            "CreatedAt": "2019-06-25T16:11:33.265Z"
        }
    ]
}
```
For more information, see [Create Bulk Deployments for Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [ListBulkDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-bulk-deployments.html) in *AWS CLI Command Reference*.

### `list-connector-definition-versions`
<a name="greengrass_ListConnectorDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-connector-definition-versions`.

**AWS CLI**
**To list the versions that are available for a connector definition**
The following `list-connector-definition-versions` example lists the versions that are available for the specified connector definition. Use the `list-connector-definitions` command to get the connector definition ID.

```
aws greengrass list-connector-definition-versions \
    --connector-definition-id {{"b5c4ebfd-f672-49a3-83cd-31c7216a7bb8"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8/versions/63c57963-c7c2-4a26-a7e2-7bf478ea2623",
            "CreationTimestamp": "2019-06-19T19:30:01.300Z",
            "Id": "b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
            "Version": "63c57963-c7c2-4a26-a7e2-7bf478ea2623"
        }
    ]
}
```
For more information, see [Integrate with Services and Protocols Using Greengrass Connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [ListConnectorDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definition-versions.html) in *AWS CLI Command Reference*.

### `list-connector-definitions`
<a name="greengrass_ListConnectorDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-connector-definitions`.

**AWS CLI**
**To list the Greengrass connectors that are defined**
The following `list-connector-definitions` example lists all of the Greengrass connectors that are defined for your AWS account.

```
aws greengrass list-connector-definitions
```
Output:

```
{
    "Definitions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
            "CreationTimestamp": "2019-06-19T19:30:01.300Z",
            "Id": "b5c4ebfd-f672-49a3-83cd-31c7216a7bb8",
            "LastUpdatedTimestamp": "2019-06-19T19:30:01.300Z",
            "LatestVersion": "63c57963-c7c2-4a26-a7e2-7bf478ea2623",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/connectors/b5c4ebfd-f672-49a3-83cd-31c7216a7bb8/versions/63c57963-c7c2-4a26-a7e2-7bf478ea2623",
            "Name": "MySNSConnector"
        }
    ]
}
```
For more information, see [Integrate with Services and Protocols Using Greengrass Connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [ListConnectorDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definitions.html) in *AWS CLI Command Reference*.

### `list-core-definition-versions`
<a name="greengrass_ListCoreDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-core-definition-versions`.

**AWS CLI**
**To list the versions of a Greengrass core definition**
The following `list-core-definitions` example lists all versions of the specified Greengrass core definition. You can use the `list-core-definitions` command to get the version ID.

```
aws greengrass list-core-definition-versions \
    --core-definition-id {{"eaf280cb-138c-4d15-af36-6f681a1348f7"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/eaf280cb-138c-4d15-af36-6f681a1348f7/versions/467c36e4-c5da-440c-a97b-084e62593b4c",
            "CreationTimestamp": "2019-06-18T16:14:17.709Z",
            "Id": "eaf280cb-138c-4d15-af36-6f681a1348f7",
            "Version": "467c36e4-c5da-440c-a97b-084e62593b4c"
        }
    ]
}
```
+  For API details, see [ListCoreDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-core-definition-versions.html) in *AWS CLI Command Reference*.

### `list-core-definitions`
<a name="greengrass_ListCoreDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-core-definitions`.

**AWS CLI**
**To list Greengrass core definitions**
The following `list-core-definitions` example lists all of the Greengrass core definitions for your AWS account.

```
aws greengrass list-core-definitions
```
Output:

```
{
    "Definitions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/0507843c-c1ef-4f06-b051-817030df7e7d",
            "CreationTimestamp": "2018-10-17T04:30:32.786Z",
            "Id": "0507843c-c1ef-4f06-b051-817030df7e7d",
            "LastUpdatedTimestamp": "2018-10-17T04:30:32.786Z",
            "LatestVersion": "bcdf9e86-3793-491e-93af-3cdfbf4e22b7",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/0507843c-c1ef-4f06-b051-817030df7e7d/versions/bcdf9e86-3793-491e-93af-3cdfbf4e22b7"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/31c22500-3509-4271-bafd-cf0655cda438",
            "CreationTimestamp": "2019-06-18T16:24:16.064Z",
            "Id": "31c22500-3509-4271-bafd-cf0655cda438",
            "LastUpdatedTimestamp": "2019-06-18T16:24:16.064Z",
            "LatestVersion": "2f350395-6d09-4c8a-8336-9ae5b57ace84",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/31c22500-3509-4271-bafd-cf0655cda438/versions/2f350395-6d09-4c8a-8336-9ae5b57ace84"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/c906ed39-a1e3-4822-a981-7b9bd57b4b46",
            "CreationTimestamp": "2019-06-18T16:21:21.351Z",
            "Id": "c906ed39-a1e3-4822-a981-7b9bd57b4b46",
            "LastUpdatedTimestamp": "2019-06-18T16:21:21.351Z",
            "LatestVersion": "42aeeac3-fd9d-4312-a8fd-ffa9404a20e0",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/c906ed39-a1e3-4822-a981-7b9bd57b4b46/versions/42aeeac3-fd9d-4312-a8fd-ffa9404a20e0"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/eaf280cb-138c-4d15-af36-6f681a1348f7",
            "CreationTimestamp": "2019-06-18T16:14:17.709Z",
            "Id": "eaf280cb-138c-4d15-af36-6f681a1348f7",
            "LastUpdatedTimestamp": "2019-06-18T16:14:17.709Z",
            "LatestVersion": "467c36e4-c5da-440c-a97b-084e62593b4c",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/eaf280cb-138c-4d15-af36-6f681a1348f7/versions/467c36e4-c5da-440c-a97b-084e62593b4c"
        }
    ]
}
```
+  For API details, see [ListCoreDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-core-definitions.html) in *AWS CLI Command Reference*.

### `list-deployments`
<a name="greengrass_ListDeployments_cli_2_topic"></a>

The following code example shows how to use `list-deployments`.

**AWS CLI**
**To list the deployments for a Greengrass group**
The following `list-deployments` example lists the deployments for the specified Greengrass group. You can use the `list-groups` command to look up your group ID.

```
aws greengrass list-deployments \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}}
```
Output:

```
{
    "Deployments": [
        {
            "CreatedAt": "2019-06-18T17:04:32.702Z",
            "DeploymentId": "1065b8a0-812b-4f21-9d5d-e89b232a530f",
            "DeploymentType": "NewDeployment",
            "GroupArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/115136b3-cfd7-4462-b77f-8741a4b00e5e"
        }
    ]
}
```
+  For API details, see [ListDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-deployments.html) in *AWS CLI Command Reference*.

### `list-device-definition-versions`
<a name="greengrass_ListDeviceDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-device-definition-versions`.

**AWS CLI**
**To list the versions of a device definition**
The following `list-device-definition-versions` example displays the device definition versions associated with the specified device definition.

```
aws greengrass list-device-definition-versions \
    --device-definition-id {{"f9ba083d-5ad4-4534-9f86-026a45df1ccd"}}
```
Output:

```
{
    "Versions": [
        {
            "Version": "83c13984-6fed-447e-84d5-5b8aa45d5f71",
            "CreationTimestamp": "2019-09-11T00:15:09.838Z",
            "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd",
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/83c13984-6fed-447e-84d5-5b8aa45d5f71"
        },
        {
            "Version": "3b5cc510-58c1-44b5-9d98-4ad858ffa795",
            "CreationTimestamp": "2019-09-11T00:11:06.197Z",
            "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd",
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/3b5cc510-58c1-44b5-9d98-4ad858ffa795"
        }
    ]
}
```
+  For API details, see [ListDeviceDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-device-definition-versions.html) in *AWS CLI Command Reference*.

### `list-device-definitions`
<a name="greengrass_ListDeviceDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-device-definitions`.

**AWS CLI**
**To list your device definitions**
The following `list-device-definitions` example displays details about the device definitions in your AWS account in the specified AWS Region.

```
aws greengrass list-device-definitions \
    --region {{us-west-2}}
```
Output:

```
{
    "Definitions": [
        {
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/50f3274c-3f0a-4f57-b114-6f46085281ab/versions/c777b0f5-1059-449b-beaa-f003ebc56c34",
            "LastUpdatedTimestamp": "2019-06-14T15:42:09.059Z",
            "LatestVersion": "c777b0f5-1059-449b-beaa-f003ebc56c34",
            "CreationTimestamp": "2019-06-14T15:42:09.059Z",
            "Id": "50f3274c-3f0a-4f57-b114-6f46085281ab",
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/50f3274c-3f0a-4f57-b114-6f46085281ab"
        },
        {
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/e01951c9-6134-479a-969a-1a15cac11c40/versions/514d57aa-4ee6-401c-9fac-938a9f7a51e5",
            "Name": "TestDeviceDefinition",
            "LastUpdatedTimestamp": "2019-04-16T23:17:43.245Z",
            "LatestVersion": "514d57aa-4ee6-401c-9fac-938a9f7a51e5",
            "CreationTimestamp": "2019-04-16T23:17:43.245Z",
            "Id": "e01951c9-6134-479a-969a-1a15cac11c40",
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/e01951c9-6134-479a-969a-1a15cac11c40"
        },
        {
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd/versions/83c13984-6fed-447e-84d5-5b8aa45d5f71",
            "Name": "TemperatureSensors",
            "LastUpdatedTimestamp": "2019-09-10T00:19:03.698Z",
            "LatestVersion": "83c13984-6fed-447e-84d5-5b8aa45d5f71",
            "CreationTimestamp": "2019-09-11T00:11:06.197Z",
            "Id": "f9ba083d-5ad4-4534-9f86-026a45df1ccd",
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/devices/f9ba083d-5ad4-4534-9f86-026a45df1ccd"
        }
    ]
}
```
+  For API details, see [ListDeviceDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-device-definitions.html) in *AWS CLI Command Reference*.

### `list-function-definition-versions`
<a name="greengrass_ListFunctionDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-function-definition-versions`.

**AWS CLI**
**To list the versions of a Lambda function**
The following `list-function-definition-versions` example lists all of the versions of the specified Lambda function. You can use the `list-function-definitions` command to get the ID.

```
aws greengrass list-function-definition-versions \
    --function-definition-id {{"063f5d1a-1dd1-40b4-9b51-56f8993d0f85"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/9748fda7-1589-4fcc-ac94-f5559e88678b",
            "CreationTimestamp": "2019-06-18T17:04:30.776Z",
            "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
            "Version": "9748fda7-1589-4fcc-ac94-f5559e88678b"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/9b08df77-26f2-4c29-93d2-769715edcfec",
            "CreationTimestamp": "2019-06-18T17:02:44.087Z",
            "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
            "Version": "9b08df77-26f2-4c29-93d2-769715edcfec"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/4236239f-94f7-4b90-a2f8-2a24c829d21e",
            "CreationTimestamp": "2019-06-18T17:01:42.284Z",
            "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
            "Version": "4236239f-94f7-4b90-a2f8-2a24c829d21e"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/343408bb-549a-4fbe-b043-853643179a39",
            "CreationTimestamp": "2019-06-18T16:21:21.431Z",
            "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
            "Version": "343408bb-549a-4fbe-b043-853643179a39"
        }
    ]
}
```
+  For API details, see [ListFunctionDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-function-definition-versions.html) in *AWS CLI Command Reference*.

### `list-function-definitions`
<a name="greengrass_ListFunctionDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-function-definitions`.

**AWS CLI**
**To list Lambda functions**
The following `list-function-definitions` example lists all of the Lambda functions defined for your AWS account.

```
aws greengrass list-function-definitions
```
Output:

```
{
    "Definitions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/017970a5-8952-46dd-b1c1-020b3ae8e960",
            "CreationTimestamp": "2018-10-17T04:30:32.884Z",
            "Id": "017970a5-8952-46dd-b1c1-020b3ae8e960",
            "LastUpdatedTimestamp": "2018-10-17T04:30:32.884Z",
            "LatestVersion": "4380b302-790d-4ed8-92bf-02e88afecb15",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/017970a5-8952-46dd-b1c1-020b3ae8e960/versions/4380b302-790d-4ed8-92bf-02e88afecb15"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
            "CreationTimestamp": "2019-06-18T16:21:21.431Z",
            "Id": "063f5d1a-1dd1-40b4-9b51-56f8993d0f85",
            "LastUpdatedTimestamp": "2019-06-18T16:21:21.431Z",
            "LatestVersion": "9748fda7-1589-4fcc-ac94-f5559e88678b",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/063f5d1a-1dd1-40b4-9b51-56f8993d0f85/versions/9748fda7-1589-4fcc-ac94-f5559e88678b"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/6598e653-a262-440c-9967-e2697f64da7b",
            "CreationTimestamp": "2019-06-18T16:24:16.123Z",
            "Id": "6598e653-a262-440c-9967-e2697f64da7b",
            "LastUpdatedTimestamp": "2019-06-18T16:24:16.123Z",
            "LatestVersion": "38bc6ccd-98a2-4ce7-997e-16c84748fae4",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/6598e653-a262-440c-9967-e2697f64da7b/versions/38bc6ccd-98a2-4ce7-997e-16c84748fae4"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/c668df84-fad2-491b-95f4-655d2cad7885",
            "CreationTimestamp": "2019-06-18T16:14:17.784Z",
            "Id": "c668df84-fad2-491b-95f4-655d2cad7885",
            "LastUpdatedTimestamp": "2019-06-18T16:14:17.784Z",
            "LatestVersion": "37dd68c4-a64f-40ba-aa13-71fecc3ebded",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/c668df84-fad2-491b-95f4-655d2cad7885/versions/37dd68c4-a64f-40ba-aa13-71fecc3ebded"
        }
    ]
}
```
+  For API details, see [ListFunctionDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-function-definitions.html) in *AWS CLI Command Reference*.

### `list-group-certificate-authorities`
<a name="greengrass_ListGroupCertificateAuthorities_cli_2_topic"></a>

The following code example shows how to use `list-group-certificate-authorities`.

**AWS CLI**
**To list the current CAs for a group**
The following `list-group-certificate-authorities` example lists the current certificate authorities (CAs) for the specified Greengrass group.

```
aws greengrass list-group-certificate-authorities \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}}
```
Output:

```
{
    "GroupCertificateAuthorities": [
        {
            "GroupCertificateAuthorityArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/certificateauthorities/f0430e1736ea8ed30cc5d5de9af67a7e3586bad9ae4d89c2a44163f65fdd8cf6",
            "GroupCertificateAuthorityId": "f0430e1736ea8ed30cc5d5de9af67a7e3586bad9ae4d89c2a44163f65fdd8cf6"
        }
    ]
}
```
+  For API details, see [ListGroupCertificateAuthorities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-group-certificate-authorities.html) in *AWS CLI Command Reference*.

### `list-group-versions`
<a name="greengrass_ListGroupVersions_cli_2_topic"></a>

The following code example shows how to use `list-group-versions`.

**AWS CLI**
**To list the versions of a Greengrass group**
The following `list-group-versions` example lists the versions of the specified Greengrass group.

```
aws greengrass list-group-versions \
    --group-id {{"1013db12-8b58-45ff-acc7-704248f66731"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/115136b3-cfd7-4462-b77f-8741a4b00e5e",
            "CreationTimestamp": "2019-06-18T17:04:30.915Z",
            "Id": "1013db12-8b58-45ff-acc7-704248f66731",
            "Version": "115136b3-cfd7-4462-b77f-8741a4b00e5e"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/4340669d-d14d-44e3-920c-46c928750750",
            "CreationTimestamp": "2019-06-18T17:03:52.663Z",
            "Id": "1013db12-8b58-45ff-acc7-704248f66731",
            "Version": "4340669d-d14d-44e3-920c-46c928750750"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/1b06e099-2d5b-4f10-91b9-78c4e060f5da",
            "CreationTimestamp": "2019-06-18T17:02:44.189Z",
            "Id": "1013db12-8b58-45ff-acc7-704248f66731",
            "Version": "1b06e099-2d5b-4f10-91b9-78c4e060f5da"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/2d3f27f1-3b43-4554-ab7a-73ec30477efe",
            "CreationTimestamp": "2019-06-18T17:01:42.401Z",
            "Id": "1013db12-8b58-45ff-acc7-704248f66731",
            "Version": "2d3f27f1-3b43-4554-ab7a-73ec30477efe"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/d20f7ae9-3444-4c1c-b025-e2ede23cdd31",
            "CreationTimestamp": "2019-06-18T16:21:21.457Z",
            "Id": "1013db12-8b58-45ff-acc7-704248f66731",
            "Version": "d20f7ae9-3444-4c1c-b025-e2ede23cdd31"
        }
    ]
}
```
+  For API details, see [ListGroupVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-group-versions.html) in *AWS CLI Command Reference*.

### `list-groups`
<a name="greengrass_ListGroups_cli_2_topic"></a>

The following code example shows how to use `list-groups`.

**AWS CLI**
**To list the Greengrass groups**
The following `list-groups` example lists all Greengrass groups that are defined in your AWS account.

```
aws greengrass list-groups
```
Output:

```
{
    "Groups": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731",
            "CreationTimestamp": "2019-06-18T16:21:21.457Z",
            "Id": "1013db12-8b58-45ff-acc7-704248f66731",
            "LastUpdatedTimestamp": "2019-06-18T16:21:21.457Z",
            "LatestVersion": "115136b3-cfd7-4462-b77f-8741a4b00e5e",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731/versions/115136b3-cfd7-4462-b77f-8741a4b00e5e",
            "Name": "GGGroup4Pi3"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1402daf9-71cf-4cfe-8be0-d5e80526d0d8",
            "CreationTimestamp": "2018-10-31T21:52:46.603Z",
            "Id": "1402daf9-71cf-4cfe-8be0-d5e80526d0d8",
            "LastUpdatedTimestamp": "2018-10-31T21:52:46.603Z",
            "LatestVersion": "749af901-60ab-456f-a096-91b12d983c29",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1402daf9-71cf-4cfe-8be0-d5e80526d0d8/versions/749af901-60ab-456f-a096-91b12d983c29",
            "Name": "MyTestGroup"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/504b5c8d-bbed-4635-aff1-48ec5b586db5",
            "CreationTimestamp": "2018-12-31T21:39:36.771Z",
            "Id": "504b5c8d-bbed-4635-aff1-48ec5b586db5",
            "LastUpdatedTimestamp": "2018-12-31T21:39:36.771Z",
            "LatestVersion": "46911e8e-f9bc-4898-8b63-59c7653636ec",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/504b5c8d-bbed-4635-aff1-48ec5b586db5/versions/46911e8e-f9bc-4898-8b63-59c7653636ec",
            "Name": "smp-ggrass-group"
        }
    ]
}
```
+  For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-groups.html) in *AWS CLI Command Reference*.

### `list-logger-definition-versions`
<a name="greengrass_ListLoggerDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-logger-definition-versions`.

**AWS CLI**
**To get a list of versions of a logger definition**
The following `list-logger-definition-versions` example gets a list of all versions of the specified logger definition.

```
aws greengrass list-logger-definition-versions \
    --logger-definition-id {{"49eeeb66-f1d3-4e34-86e3-3617262abf23"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23/versions/5e3f6f64-a565-491e-8de0-3c0d8e0f2073",
            "CreationTimestamp": "2019-05-08T16:10:13.866Z",
            "Id": "49eeeb66-f1d3-4e34-86e3-3617262abf23",
            "Version": "5e3f6f64-a565-491e-8de0-3c0d8e0f2073"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23/versions/3ec6d3af-eb85-48f9-a16d-1c795fe696d7",
            "CreationTimestamp": "2019-05-08T16:10:13.809Z",
            "Id": "49eeeb66-f1d3-4e34-86e3-3617262abf23",
            "Version": "3ec6d3af-eb85-48f9-a16d-1c795fe696d7"
        }
    ]
}
```
+  For API details, see [ListLoggerDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-logger-definition-versions.html) in *AWS CLI Command Reference*.

### `list-logger-definitions`
<a name="greengrass_ListLoggerDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-logger-definitions`.

**AWS CLI**
**To get a list of logger definitions**
The following `list-logger-definitions` example lists all of the logger definitions for your AWS account.

```
aws greengrass list-logger-definitions
```
Output:

```
{
    "Definitions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23",
            "CreationTimestamp": "2019-05-08T16:10:13.809Z",
            "Id": "49eeeb66-f1d3-4e34-86e3-3617262abf23",
            "LastUpdatedTimestamp": "2019-05-08T16:10:13.809Z",
            "LatestVersion": "5e3f6f64-a565-491e-8de0-3c0d8e0f2073",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/loggers/49eeeb66-f1d3-4e34-86e3-3617262abf23/versions/5e3f6f64-a565-491e-8de0-3c0d8e0f2073"
        }
    ]
}
```
+  For API details, see [ListLoggerDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-logger-definitions.html) in *AWS CLI Command Reference*.

### `list-resource-definition-versions`
<a name="greengrass_ListResourceDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-resource-definition-versions`.

**AWS CLI**
**To list the versions of a resource definition**
The following `list-resource-definition-versions` example lists the versions for the specified Greengrass resource.

```
aws greengrass list-resource-definition-versions \
    --resource-definition-id {{"ad8c101d-8109-4b0e-b97d-9cc5802ab658"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658/versions/26e8829a-491a-464d-9c87-664bf6f6f2be",
            "CreationTimestamp": "2019-06-19T16:40:59.392Z",
            "Id": "ad8c101d-8109-4b0e-b97d-9cc5802ab658",
            "Version": "26e8829a-491a-464d-9c87-664bf6f6f2be"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658/versions/432d92f6-12de-4ec9-a704-619a942a62aa",
            "CreationTimestamp": "2019-06-19T16:40:59.261Z",
            "Id": "ad8c101d-8109-4b0e-b97d-9cc5802ab658",
            "Version": "432d92f6-12de-4ec9-a704-619a942a62aa"
        }
    ]
}
```
+  For API details, see [ListResourceDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-resource-definition-versions.html) in *AWS CLI Command Reference*.

### `list-resource-definitions`
<a name="greengrass_ListResourceDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-resource-definitions`.

**AWS CLI**
**To list the resources that are defined**
The following `list-resource-definitions` example lists the resources that are defined for AWS IoT Greengrass to use.

```
aws greengrass list-resource-definitions
```
Output:

```
{
    "Definitions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658",
            "CreationTimestamp": "2019-06-19T16:40:59.261Z",
            "Id": "ad8c101d-8109-4b0e-b97d-9cc5802ab658",
            "LastUpdatedTimestamp": "2019-06-19T16:40:59.261Z",
            "LatestVersion": "26e8829a-491a-464d-9c87-664bf6f6f2be",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658/versions/26e8829a-491a-464d-9c87-664bf6f6f2be"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38",
            "CreationTimestamp": "2019-06-19T21:51:28.212Z",
            "Id": "c8bb9ebc-c3fd-40a4-9c6a-568d75569d38",
            "LastUpdatedTimestamp": "2019-06-19T21:51:28.212Z",
            "LatestVersion": "a5f94d0b-f6bc-40f4-bb78-7a1c5fe13ba1",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38/versions/a5f94d0b-f6bc-40f4-bb78-7a1c5fe13ba1",
            "Name": "MyGreengrassResources"
        }
    ]
}
```
+  For API details, see [ListResourceDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-resource-definitions.html) in *AWS CLI Command Reference*.

### `list-subscription-definition-versions`
<a name="greengrass_ListSubscriptionDefinitionVersions_cli_2_topic"></a>

The following code example shows how to use `list-subscription-definition-versions`.

**AWS CLI**
**To list the versions of a subscription definition**
The following `list-subscription-definition-versions` example lists all versions of the specified subscription. You can use the `list-subscription-definitions` command to look up the subscription ID.

```
aws greengrass list-subscription-definition-versions \
    --subscription-definition-id {{"70e49321-83d5-45d2-bc09-81f4917ae152"}}
```
Output:

```
{
    "Versions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152/versions/88ae8699-12ac-4663-ba3f-4d7f0519140b",
            "CreationTimestamp": "2019-06-18T17:03:52.499Z",
            "Id": "70e49321-83d5-45d2-bc09-81f4917ae152",
            "Version": "88ae8699-12ac-4663-ba3f-4d7f0519140b"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152/versions/7e320ba3-c369-4069-a2f0-90acb7f219d6",
            "CreationTimestamp": "2019-06-18T17:03:52.392Z",
            "Id": "70e49321-83d5-45d2-bc09-81f4917ae152",
            "Version": "7e320ba3-c369-4069-a2f0-90acb7f219d6"
        }
    ]
}
```
+  For API details, see [ListSubscriptionDefinitionVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-subscription-definition-versions.html) in *AWS CLI Command Reference*.

### `list-subscription-definitions`
<a name="greengrass_ListSubscriptionDefinitions_cli_2_topic"></a>

The following code example shows how to use `list-subscription-definitions`.

**AWS CLI**
**To get a list subscription definitions**
The following `list-subscription-definitions` example lists all of the AWS IoT Greengrass subscriptions that are defined in your AWS account.

```
aws greengrass list-subscription-definitions
```
Output:

```
{
    "Definitions": [
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152",
            "CreationTimestamp": "2019-06-18T17:03:52.392Z",
            "Id": "70e49321-83d5-45d2-bc09-81f4917ae152",
            "LastUpdatedTimestamp": "2019-06-18T17:03:52.392Z",
            "LatestVersion": "88ae8699-12ac-4663-ba3f-4d7f0519140b",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/70e49321-83d5-45d2-bc09-81f4917ae152/versions/88ae8699-12ac-4663-ba3f-4d7f0519140b"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/cd6f1c37-d9a4-4e90-be94-01a7404f5967",
            "CreationTimestamp": "2018-10-18T15:45:34.024Z",
            "Id": "cd6f1c37-d9a4-4e90-be94-01a7404f5967",
            "LastUpdatedTimestamp": "2018-10-18T15:45:34.024Z",
            "LatestVersion": "d1cf8fac-284f-4f6a-98fe-a2d36d089373",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/cd6f1c37-d9a4-4e90-be94-01a7404f5967/versions/d1cf8fac-284f-4f6a-98fe-a2d36d089373"
        },
        {
            "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/fa81bc84-3f59-4377-a84b-5d0134da359b",
            "CreationTimestamp": "2018-10-22T17:09:31.429Z",
            "Id": "fa81bc84-3f59-4377-a84b-5d0134da359b",
            "LastUpdatedTimestamp": "2018-10-22T17:09:31.429Z",
            "LatestVersion": "086d1b08-b25a-477c-a16f-6f9b3a9c295a",
            "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/subscriptions/fa81bc84-3f59-4377-a84b-5d0134da359b/versions/086d1b08-b25a-477c-a16f-6f9b3a9c295a"
        }
    ]
}
```
+  For API details, see [ListSubscriptionDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-subscription-definitions.html) in *AWS CLI Command Reference*.

### `list-tags-for-resource`
<a name="greengrass_ListTagsForResource_cli_2_topic"></a>

The following code example shows how to use `list-tags-for-resource`.

**AWS CLI**
**To list the tags attached to a resource**
The following `list-tags-for-resource` example lists the tags and their values that are attached to the specified resource.

```
aws greengrass list-tags-for-resource \
    --resource-arn {{"arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658"}}
```
Output:

```
{
    "tags": {
        "ResourceSubType": "USB",
        "ResourceType": "Device"
    }
}
```
For more information, see [Tagging Your Greengrass Resources](https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-tags-for-resource.html) in *AWS CLI Command Reference*.

### `reset-deployments`
<a name="greengrass_ResetDeployments_cli_2_topic"></a>

The following code example shows how to use `reset-deployments`.

**AWS CLI**
**To clean up deployment information for a Greengrass group**
The following `reset-deployments` example cleans up deployment information for the specified Greengrass group. When you add the `--force option`, the deployment information is reset without waiting for the core device to respond.

```
aws greengrass reset-deployments \
    --group-id {{"1402daf9-71cf-4cfe-8be0-d5e80526d0d8"}} \
    --force
```
Output:

```
{
    "DeploymentArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1402daf9-71cf-4cfe-8be0-d5e80526d0d8/deployments/7dd4e356-9882-46a3-9e28-6d21900c011a",
    "DeploymentId": "7dd4e356-9882-46a3-9e28-6d21900c011a"
}
```
For more information, see [Reset Deployments](https://docs.aws.amazon.com/greengrass/latest/developerguide/reset-deployments-scenario.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [ResetDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/reset-deployments.html) in *AWS CLI Command Reference*.

### `start-bulk-deployment`
<a name="greengrass_StartBulkDeployment_cli_2_topic"></a>

The following code example shows how to use `start-bulk-deployment`.

**AWS CLI**
**To start a bulk deployment operation**
The following `start-bulk-deployment` example starts a bulk deployment operation, using a file stored in an S3 bucket to specify the groups to be deployed.

```
aws greengrass start-bulk-deployment \
    --cli-input-json "{\"InputFileUri\":\"https://gg-group-deployment1.s3-us-west-2.amazonaws.com/MyBulkDeploymentInputFile.txt\", \"ExecutionRoleArn\":\"arn:aws:iam::123456789012:role/ggCreateDeploymentRole\",\"AmznClientToken\":\"yourAmazonClientToken\"}"
```
Output:

```
{
    "BulkDeploymentArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/bulk/deployments/870fb41b-6288-4e0c-bc76-a7ba4b4d3267",
    "BulkDeploymentId": "870fb41b-6288-4e0c-bc76-a7ba4b4d3267"
}
```
For more information, see [Create Bulk Deployments for Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [StartBulkDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/start-bulk-deployment.html) in *AWS CLI Command Reference*.

### `stop-bulk-deployment`
<a name="greengrass_StopBulkDeployment_cli_2_topic"></a>

The following code example shows how to use `stop-bulk-deployment`.

**AWS CLI**
**To stop a bulk deployment**
The following `stop-bulk-deployment` example stops the specified bulk deployment. If you try to stop a bulk deployment that is complete, you receive an error: `InvalidInputException: Cannot change state of finished execution.`

```
aws greengrass stop-bulk-deployment \
    --bulk-deployment-id {{"870fb41b-6288-4e0c-bc76-a7ba4b4d3267"}}
```
This command produces no output.
For more information, see [Create Bulk Deployments for Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [StopBulkDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/stop-bulk-deployment.html) in *AWS CLI Command Reference*.

### `tag-resource`
<a name="greengrass_TagResource_cli_2_topic"></a>

The following code example shows how to use `tag-resource`.

**AWS CLI**
**To apply tags to a resource**
The following `tag-resource` example applies two tags, `ResourceType` and `ResourceSubType`, to the specified Greengrass resource. This operation can both add new tags and values or update the value for existing tags. Use the `untag-resource` command to remove a tag.

```
aws greengrass tag-resource \
    --resource-arn {{"arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/ad8c101d-8109-4b0e-b97d-9cc5802ab658"}} \
    --tags {{"ResourceType=Device,ResourceSubType=USB"}}
```
This command produces no output.
For more information, see [Tagging Your Greengrass Resources](https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/tag-resource.html) in *AWS CLI Command Reference*.

### `untag-resource`
<a name="greengrass_UntagResource_cli_2_topic"></a>

The following code example shows how to use `untag-resource`.

**AWS CLI**
**To remove a tag and its value from a resource**
The following `untag-resource` example removes the tag whose key is `Category` from the specified Greengrass group. If the key `Category` does not exist for the specified resource, no error is returned.

```
aws greengrass untag-resource \
    --resource-arn {{"arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/1013db12-8b58-45ff-acc7-704248f66731"}} \
    --tag-keys {{"Category"}}
```
This command produces no output.
For more information, see [Tagging Your Greengrass Resources](https://docs.aws.amazon.com/greengrass/latest/developerguide/tagging.html) in the **AWS IoT Greengrass Developer Guide**.
+  For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/untag-resource.html) in *AWS CLI Command Reference*.

### `update-connectivity-info`
<a name="greengrass_UpdateConnectivityInfo_cli_2_topic"></a>

The following code example shows how to use `update-connectivity-info`.

**AWS CLI**
**To update the connectivity information for a Greengrass core**
The following `update-connectivity-info` example changes the endpoints that devices can use to connect to the specified Greengrass core. Connectivity information is a list of IP addresses or domain names, with corresponding port numbers and optional customer-defined metadata. You might need to update connectivity information when the local network changes.

```
aws greengrass update-connectivity-info \
    --thing-name {{"MyGroup_Core"}} \
    --connectivity-info "[{\"Metadata\":\"\",\"PortNumber\":8883,\"HostAddress\":\"127.0.0.1\",\"Id\":\"localhost_127.0.0.1_0\"},{\"Metadata\":\"\",\"PortNumber\":8883,\"HostAddress\":\"192.168.1.3\",\"Id\":\"localIP_192.168.1.3\"}]"
```
Output:

```
{
    "Version": "312de337-59af-4cf9-a278-2a23bd39c300"
}
```
+  For API details, see [UpdateConnectivityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-connectivity-info.html) in *AWS CLI Command Reference*.

### `update-connector-definition`
<a name="greengrass_UpdateConnectorDefinition_cli_2_topic"></a>

The following code example shows how to use `update-connector-definition`.

**AWS CLI**
**To update the name for a connector definition**
The following `update-connector-definition` example updates the name for the specified connector definition. If you want to update the details for the connector, use the `create-connector-definition-version` command to create a new version.

```
aws greengrass update-connector-definition \
    --connector-definition-id {{"55d0052b-0d7d-44d6-b56f-21867215e118"}} \
    --name {{"GreengrassConnectors2019"}}
```
For more information, see [Integrate with Services and Protocols Using Connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateConnectorDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-connector-definition.html) in *AWS CLI Command Reference*.

### `update-core-definition`
<a name="greengrass_UpdateCoreDefinition_cli_2_topic"></a>

The following code example shows how to use `update-core-definition`.

**AWS CLI**
**To update a core definition**
The following `update-core-definition` example changes the name of the specified core definition. You can update only the `name` property of a core definition.

```
aws greengrass update-core-definition \
    --core-definition-id {{"582efe12-b05a-409e-9a24-a2ba1bcc4a12"}} \
    --name {{"MyCoreDevices"}}
```
This command produces no output.
For more information, see [Configure the AWS IoT Greengrass Core](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-core.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateCoreDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-core-definition.html) in *AWS CLI Command Reference*.

### `update-device-definition`
<a name="greengrass_UpdateDeviceDefinition_cli_2_topic"></a>

The following code example shows how to use `update-device-definition`.

**AWS CLI**
**To update a device definition**
The following `update-device-definition` example changes the name of the specified device definition. You can only update the `name` property of a device definition.

```
aws greengrass update-device-definition \
    --device-definition-id {{"f9ba083d-5ad4-4534-9f86-026a45df1ccd"}} \
    --name {{"TemperatureSensors"}}
```
This command produces no output.
+  For API details, see [UpdateDeviceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-device-definition.html) in *AWS CLI Command Reference*.

### `update-function-definition`
<a name="greengrass_UpdateFunctionDefinition_cli_2_topic"></a>

The following code example shows how to use `update-function-definition`.

**AWS CLI**
**To update the name for a function definition**
The following `update-function-definition` example updates the name for the specified function definition. If you want to update the details for the function, use the `create-function-definition-version` command to create a new version.

```
aws greengrass update-function-definition \
    --function-definition-id {{"e47952bd-dea9-4e2c-a7e1-37bbe8807f46"}} \
    --name {{ObsoleteFunction}}
```
This command produces no output.
For more information, see [Run Local Lambda Functions](https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-functions.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateFunctionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-function-definition.html) in *AWS CLI Command Reference*.

### `update-group-certificate-configuration`
<a name="greengrass_UpdateGroupCertificateConfiguration_cli_2_topic"></a>

The following code example shows how to use `update-group-certificate-configuration`.

**AWS CLI**
**To update the expiry of a group's certificates**
The following `update-group-certificate-configuration` example sets a 10-day expiry for the certificates generated for the specified group.

```
aws greengrass update-group-certificate-configuration \
    --group-id {{"8eaadd72-ce4b-4f15-892a-0cc4f3a343f1"}} \
    --certificate-expiry-in-milliseconds {{864000000}}
```
Output:

```
{
    "CertificateExpiryInMilliseconds": 864000000,
    "CertificateAuthorityExpiryInMilliseconds": 2524607999000,
    "GroupId": "8eaadd72-ce4b-4f15-892a-0cc4f3a343f1"
}
```
For more information, see [AWS IoT Greengrass Security](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-sec.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateGroupCertificateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-group-certificate-configuration.html) in *AWS CLI Command Reference*.

### `update-group`
<a name="greengrass_UpdateGroup_cli_2_topic"></a>

The following code example shows how to use `update-group`.

**AWS CLI**
**To update the group name**
The following `update-group` example updates the name of the specified Greengrass group. If you want to update the details for the group, use the `create-group-version` command to create a new version.

```
aws greengrass update-group \
    --group-id {{"1402daf9-71cf-4cfe-8be0-d5e80526d0d8"}} \
    --name {{TestGroup4of6}}
```
For more information, see [Configure AWS IoT Greengrass on AWS IoT](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-config.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-group.html) in *AWS CLI Command Reference*.

### `update-logger-definition`
<a name="greengrass_UpdateLoggerDefinition_cli_2_topic"></a>

The following code example shows how to use `update-logger-definition`.

**AWS CLI**
**To update a logger definition**
The following `update-logger-definition` example changes the name of the specified logger definition. You can only update the `name` property of a logger definition.

```
aws greengrass update-logger-definition \
    --logger-definition-id {{"a454b62a-5d56-4ca9-bdc4-8254e1662cb0"}} \
    --name {{"LoggingConfigsForSensors"}}
```
This command produces no output.
For more information, see [Monitoring with AWS IoT Greengrass Logs](https://docs.aws.amazon.com/greengrass/latest/developerguide/greengrass-logs-overview.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateLoggerDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-logger-definition.html) in *AWS CLI Command Reference*.

### `update-resource-definition`
<a name="greengrass_UpdateResourceDefinition_cli_2_topic"></a>

The following code example shows how to use `update-resource-definition`.

**AWS CLI**
**To update the name for a resource definition**
The following `update-resource-definition` example updates the name for the specified resource definition. If you want to change the details for the resource, use the `create-resource-definition-version` command to create a new version.

```
aws greengrass update-resource-definition \
    --resource-definition-id {{"c8bb9ebc-c3fd-40a4-9c6a-568d75569d38"}} \
    --name {{GreengrassConnectorResources}}
```
This command produces no output.
For more information, see [Access Local Resources with Lambda Functions and Connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateResourceDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-resource-definition.html) in *AWS CLI Command Reference*.

### `update-subscription-definition`
<a name="greengrass_UpdateSubscriptionDefinition_cli_2_topic"></a>

The following code example shows how to use `update-subscription-definition`.

**AWS CLI**
**To update the name for a subscription definition**
The following `update-subscription-definition` example updates the name for the specified subscription definition. If you want to change details for the subscription, use the `create-subscription-definition-version` command to create a new version.

```
aws greengrass update-subscription-definition \
    --subscription-definition-id {{"fa81bc84-3f59-4377-a84b-5d0134da359b"}} \
    --name {{"ObsoleteSubscription"}}
```
This command produces no output.
For more information, see title in the *guide*.
+  For API details, see [UpdateSubscriptionDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-subscription-definition.html) in *AWS CLI Command Reference*.

### `update-thing-runtime-configuration`
<a name="greengrass_UpdateThingRuntimeConfiguration_cli_2_topic"></a>

The following code example shows how to use `update-thing-runtime-configuration`.

**AWS CLI**
**To turn on telemetry in the runtime configuration of a Greengrass core**
The following `update-thing-runtime-configuration` example updates the runtime configuration of a Greengrass core to turn on telemetry.

```
aws greengrass update-thing-runtime-configuration \
    --thing-name {{SampleGreengrassCore}} \
    --telemetry-configuration {\"Telemetry\":\"On\"}
```
This command produces no output.
For more information, see [Configuring telemetry settings](https://docs.aws.amazon.com/greengrass/latest/developerguide/telemetry.html#configure-telemetry-settings) in the *AWS IoT Greengrass Developer Guide*.
+  For API details, see [UpdateThingRuntimeConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-thing-runtime-configuration.html) in *AWS CLI Command Reference*.
