---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/FIPS.html
---

# FIPS endpoints
<a name="FIPS"></a>

AWS IoT Greengrass supports the use of FIPS ([Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/)) endpoints. When FIPS mode is enabled, all data transmissions, including both HTTP and MQTT protocols, to AWS Cloud services should invoke and establish connections with the corresponding FIPS-compliant endpoints ([FIPS - Amazon Web Services (AWS)](https://aws.amazon.com/compliance/fips/)).

MQTT communications to AWS IoT utilize the IoT dataplane FIPS endpoint ([Connecting to AWS IoT FIPS endpoints - AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-connect-fips.html#iot-connect-fips-data)) and the AWS-developed FIPS-compliant cryptographic library aws-lc.

For HTTP communications in Greengrass:
+ For nucleus and plugin components, all SDK HTTP clients are configured with FIPS endpoints by setting the system property AWS\_USE\_FIPS\_ENDPOINT to true;
+ For generic components, all components start with the system property AWS\_USE\_FIPS\_ENDPOINT set to true. This process ensures that the SDK HTTP clients used by these generic components send requests to FIPS-compliant endpoints.

**Note**
In the case of Stream manager, Nucleus passes the environment variable AWS\_GG\_FIPS\_MODE. This environment variable allows the HTTP clients utilized within the Stream Manager to identify and connect to the corresponding FIPS-compliant endpoint.

AWS IoT Greengrass offers two methods to enable FIPS mode: provisioning and deployment. To activate the FIPS mode, you have to set the configuration parameter `fipsMode` to true, Nucleus then sets the system property AWS\_USE\_FIPS\_ENDPOINT to true and propagate it as an environment variable to all other components. Additionally, AWS IoT Greengrass will download a root CA certificate (CA3) and append it to the existing rootCA.pem (or AmazonRootCA1.pem) file. If you enable FIPS through a new deployment, Nucleus will restart to ensure that the system property takes effect after enabling FIPS mode.

 Apart from configuring the `fipsMode` parameter, you must also configure the `iotDataEndpoint`, `iotCredEndpoint` and `greengrassDataEndpoint` parameters. For more information, see the relevant document below.

## Enable FIPS endpoints with deployment
<a name="FIPS-deployment"></a>

Get the AWS IoT endpoints for your AWS account, and save them to use later. Your device uses these endpoints to connect to AWS IoT. There are two endpoints required, the `iotDataEndpoint` and the `iotCredEndpoint`. Do the following:

1. Get the FIPS data endpoint for your region in the [AWS IoT Core FIPS data plane endpoints.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints) The FIPS data endpoint for your AWS account should look like this: {{data.iot-fips.us-west-2.amazonaws.com}}

1. Get the FIPS credentials endpoint for your region in the [AWS IoT Core FIPS data plane endpoints.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints) The FIPS credentials endpoint for your AWS account should look like this: {{data.credentials.iot-fips.us-west-2.amazonaws.com}}

Then, to enable FIPS with a deployment, you need to apply the following configuration to Nucleus. The configuration to merge on the deployment is as follows.

------
#### [ Console ]

**Configuration to merge**

```
{
  "fipsMode": "true",
  "iotDataEndpoint": "data.iot-fips.us-west-2.amazonaws.com",
  "greengrassDataPlaneEndpoint": "iotData",
  "iotCredEndpoint": "data.credentials.iot-fips.us-west-2.amazonaws.com"
}
```

------
#### [ AWS CLI ]

The following command creates a deployment to a core device.

```
aws greengrassv2 create-deployment --cli-input-json file://dashboard-deployment.json
```

The `dashboard-deployment.json` file contains the following JSON document.

```
{
  "targetArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore",
  "deploymentName": "Deployment for MyGreengrassCore",
  "components": {
    "aws.greengrass.Nucleus": {
      "componentVersion": "2.13.0",
      "configurationUpdate": {
        "merge":{\"fipsMode\":\"true\",\"iotDataEndpoint\":\"data.iot-fips.us-west-2.amazonaws.com\",\"greengrassDataPlaneEndpoint\":\"iotData\",\"iotCredEndpoint\":\"data.credentials.iot-fips.us-west-2.amazonaws.com\"}"
      }
    }
  }
}
```

------
#### [ Greengrass CLI ]

The following [Greengrass CLI](greengrass-cli-component.md) command creates a local deployment on a core device.

```
sudo greengrass-cli deployment create \
  --recipeDir recipes \
  --artifactDir artifacts \
  --merge "aws.greengrass.Nucleus=2.13.0" \
  --update-config dashboard-configuration.json
```

The `dashboard-configuration.json` file contains the following JSON document.

```
{
  "aws.greengrass.Nucleus": {
    "MERGE": {
       "fipsMode": "true",
       "iotDataEndpoint": "data.iot-fips.us-west-2.amazonaws.com",
       "greengrassDataPlaneEndpoint": "iotData",
       "iotCredEndpoint": "data.credentials.iot-fips.us-west-2.amazonaws.com"

    }
  }
}
```

------

## Install Nucleus with FIPS endpoints with manual resource provisioning
<a name="FIPS-manual-installation"></a>

Manually provision AWS resources for AWS IoT Greengrass V2 core devices with FIPS endpoints

**Important**  <a name="install-greengrass-core-requirements-note"></a>
Before you download the AWS IoT Greengrass Core software, check that your core device meets the [requirements](greengrass-nucleus-component.md#greengrass-v2-requirements) to install and run the AWS IoT Greengrass Core software v2.0.

**Topics**
+ [Retrieve AWS IoT endpoints](#w2ab1c58c44c23b9)
+ [Create an AWS IoT thing](#create-iot-thing)
+ [Create the thing certificate](#create-thing-certificate-fips)
+ [Create a token exchange role](#create-token-exchange-role)
+ [Download certificates to the device](#download-thing-certificates)
+ [Set up the device environment](#set-up-device-environment)
+ [Download the AWS IoT Greengrass Core software](#download-greengrass-core-v2)
+ [Install the AWS IoT Greengrass Core software](#run-greengrass-core-v2-installer-manual-fips)

### Retrieve AWS IoT endpoints
<a name="w2ab1c58c44c23b9"></a>

Get the AWS IoT endpoints for your AWS account, and save them to use later. Your device uses these endpoints to connect to AWS IoT. There are two endpoints required, the `iotDataEndpoint` and the `iotCredEndpoint`. Do the following:

1. Get the FIPS data endpoint for your region in the [AWS IoT Core FIPS data plane endpoints.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints) The FIPS data endpoint for your AWS account should look like this: {{data.iot-fips.us-west-2.amazonaws.com}}

1. Get the FIPS credentials endpoint for your region in the [AWS IoT Core FIPS data plane endpoints.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints) The FIPS credentials endpoint for your AWS account should look like this: {{data.credentials.iot-fips.us-west-2.amazonaws.com}}

### Create an AWS IoT thing
<a name="create-iot-thing"></a>

AWS IoT *things* represent devices and logical entities that connect to AWS IoT. Greengrass core devices are AWS IoT things. When you register a device as an AWS IoT thing, that device can use a digital certificate to authenticate with AWS.

In this section, you create an AWS IoT thing that represents your device.

**To create an AWS IoT thing**

1. Create an AWS IoT thing for your device. On your development computer, run the following command.
   + Replace {{MyGreengrassCore}} with the thing name to use. This name is also the name of your Greengrass core device.
**Note**  <a name="install-argument-thing-name-constraint"></a>
The thing name can't contain colon (`:`) characters.

   ```
   aws iot create-thing --thing-name {{MyGreengrassCore}}
   ```

   The response looks similar to the following example, if the request succeeds.

   ```
   {
     "thingName": "MyGreengrassCore",
     "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore",
     "thingId": "8cb4b6cd-268e-495d-b5b9-1713d71dbf42"
   }
   ```

1. (Optional) Add the AWS IoT thing to a new or existing thing group. You use thing groups to manage fleets of Greengrass core devices. When you deploy software components to your devices, you can target individual devices or groups of devices. You can add a device to a thing group with an active Greengrass deployment to deploy that thing group's software components to the device. Do the following:

   1. (Optional) Create an AWS IoT thing group.
      + Replace {{MyGreengrassCoreGroup}} with the name of the thing group to create.
**Note**  <a name="install-argument-thing-group-name-constraint"></a>
The thing group name can't contain colon (`:`) characters.

      ```
      aws iot create-thing-group --thing-group-name {{MyGreengrassCoreGroup}}
      ```

      The response looks similar to the following example, if the request succeeds.

      ```
      {
        "thingGroupName": "MyGreengrassCoreGroup",
        "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup",
        "thingGroupId": "4df721e1-ff9f-4f97-92dd-02db4e3f03aa"
      }
      ```

   1. Add the AWS IoT thing to a thing group.
      + Replace {{MyGreengrassCore}} with the name of your AWS IoT thing.
      + Replace {{MyGreengrassCoreGroup}} with the name of the thing group.

      ```
      aws iot add-thing-to-thing-group --thing-name {{MyGreengrassCore}} --thing-group-name {{MyGreengrassCoreGroup}}
      ```

      The command doesn't have any output if the request succeeds.

### Create the thing certificate
<a name="create-thing-certificate-fips"></a>

<a name="create-thing-certificate-intro-1"></a>When you register a device as an AWS IoT thing, that device can use a digital certificate to authenticate with AWS. This certificate allows the device to communicate with AWS IoT and AWS IoT Greengrass.

<a name="create-thing-certificate-intro-2"></a>In this section, you create and download certificates that your device can use to connect to AWS.

<a name="create-thing-certificate-intro-3"></a>If you want to configure the AWS IoT Greengrass Core software to use a hardware security module (HSM) to securely store the private key and certificate, follow the steps to create the certificate from a private key in an HSM. Otherwise, follow the steps to create the certificate and private key in the AWS IoT service. The hardware security feature is available on Linux devices only. For more information about hardware security and requirements to use it, see [Hardware security integration](hardware-security.md).

#### Create the certificate and private key in the AWS IoT service
<a name="create-thing-certificate-cloud"></a><a name="create-thing-certificate-cloud-steps"></a>

**To create the thing certificate**

1. Create a folder where you download the certificates for the AWS IoT thing.

   ```
   mkdir greengrass-v2-certs
   ```

1. Create and download the certificates for the AWS IoT thing.

   ```
   aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile greengrass-v2-certs/device.pem.crt --public-key-outfile greengrass-v2-certs/public.pem.key --private-key-outfile greengrass-v2-certs/private.pem.key
   ```

   The response looks similar to the following example, if the request succeeds.

   ```
   {
     "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4",
     "certificateId": "aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4",
     "certificatePem": "-----BEGIN CERTIFICATE-----
   MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w
    0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZ
    WF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIw
    EAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5
    jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBh
    MCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBb
    WF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMx
    HzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQE
    BBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVI
    k60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQ
    ITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nr
    AgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auN
    KyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6Guo
    EDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw
    3rrszlaEXAMPLE=
   -----END CERTIFICATE-----",
     "keyPair": {
       "PublicKey": "-----BEGIN PUBLIC KEY-----\
   MIIBIjANBgkqhkEXAMPLEQEFAAOCAQ8AMIIBCgKCAQEAEXAMPLE1nnyJwKSMHw4h\
   MMEXAMPLEuuN/dMAS3fyce8DW/4+EXAMPLEyjmoF/YVF/gHr99VEEXAMPLE5VF13\
   59VK7cEXAMPLE67GK+y+jikqXOgHh/xJTwo+sGpWEXAMPLEDz18xOd2ka4tCzuWEXAMPLEahJbYkCPUBSU8opVkR7qkEXAMPLE1DR6sx2HocliOOLtu6Fkw91swQWEXAMPLE\\GB3ZPrNh0PzQYvjUStZeccyNCx2EXAMPLEvp9mQOUXP6plfgxwKRX2fEXAMPLEDa\
   hJLXkX3rHU2xbxJSq7D+XEXAMPLEcw+LyFhI5mgFRl88eGdsAEXAMPLElnI9EesG\
   FQIDAQAB\
   -----END PUBLIC KEY-----\
   ",
       "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\
   key omitted for security reasons\
   -----END RSA PRIVATE KEY-----\
   "
     }
   }
   ```

   Save the certificate's Amazon Resource Name (ARN) to use to configure the certificate later.

#### Create the certificate from a private key in an HSM
<a name="create-thing-certificate-hardware-security"></a>

**Note**
This feature is available for v2.5.3 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md). AWS IoT Greengrass doesn't currently support this feature on Windows core devices.

**To create the thing certificate**

1. On the core device, initialize a PKCS\#11 token in the HSM, and generate a private key. The private key must be an RSA key with an RSA-2048 key size (or larger) or an ECC key.
**Note**  <a name="hardware-security-module-requirements-key-notes"></a>
To use a hardware security module with ECC keys, you must use [Greengrass nucleus](greengrass-nucleus-component.md) v2.5.6 or later.
To use a hardware security module and [secret manager](secret-manager-component.md), you must use a hardware security module with RSA keys.

   Check the documentation for your HSM to learn how to initialize the token and generate the private key. If your HSM supports object IDs, specify an object ID when you generate the private key. Save the slot ID, user PIN, object label, object ID (if your HSM uses one) that you specify when you initialize the token and generate the private key. You use these values later when you import the thing certificate to the HSM and configure the AWS IoT Greengrass Core software.

1. Create a certificate signing request (CSR) from the private key. AWS IoT uses this CSR to create a thing certificate for the private key that you generated in the HSM. For information about how to create a CSR from the private key, see the documentation for your HSM. The CSR is a file, such as `iotdevicekey.csr`.

1. Copy the CSR from the device to your development computer. If SSH and SCP are enabled on the development computer and the device, you can use the `scp` command on your development computer to transfer the CSR. Replace {{device-ip-address}} with the IP address of your device, and replace {{\~/iotdevicekey.csr}} with the path to the CSR file on the device.

   ```
   scp {{device-ip-address}}:{{~/iotdevicekey.csr}} iotdevicekey.csr
   ```

1. On your development computer, create a folder where you download the certificate for the AWS IoT thing.

   ```
   mkdir greengrass-v2-certs
   ```

1. Use the CSR file to create and download the certificate for the AWS IoT thing to your development computer.

   ```
   aws iot create-certificate-from-csr --set-as-active --certificate-signing-request=file://iotdevicekey.csr --certificate-pem-outfile greengrass-v2-certs/device.pem.crt
   ```

   The response looks similar to the following example, if the request succeeds.

   ```
   {
     "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4",
     "certificateId": "aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4",
     "certificatePem": "-----BEGIN CERTIFICATE-----
   MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w
    0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZ
    WF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIw
    EAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5
    jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBh
    MCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBb
    WF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMx
    HzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQE
    BBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVI
    k60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQ
    ITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nr
    AgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auN
    KyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6Guo
    EDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw
    3rrszlaEXAMPLE=
   -----END CERTIFICATE-----"
   }
   ```

   Save the certificate's ARN to use to configure the certificate later.

Next, configure the thing certificate. For more information, see [Configure the thing certificate](manual-installation.md#configure-thing-certificate).

### Create a token exchange role
<a name="create-token-exchange-role"></a>

<a name="installation-create-token-exchange-role-intro"></a>Greengrass core devices use an IAM service role, called the *token exchange role*, to authorize calls to AWS services. The device uses the AWS IoT credentials provider to get temporary AWS credentials for this role, which allows the device to interact with AWS IoT, send logs to Amazon CloudWatch Logs, and download custom component artifacts from Amazon S3. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).

<a name="installation-create-token-exchange-role-alias-intro"></a>You use an AWS IoT *role alias* to configure the token exchange role for Greengrass core devices. Role aliases enable you to change the token exchange role for a device but keep the device configuration the same. For more information, see [Authorizing direct calls to AWS services](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html) in the *AWS IoT Core Developer Guide*.

In this section, you create a token exchange IAM role and an AWS IoT role alias that points to the role. If you have already set up a Greengrass core device, you can use its token exchange role and role alias instead of creating new ones. Then, you configure your device's AWS IoT thing to use that role and alias.

**To create a token exchange IAM role**

1. <a name="create-token-exchange-role-create-iam-role"></a>Create an IAM role that your device can use as a token exchange role. Do the following:

   1. Create a file that contains the trust policy document that the token exchange role requires.

      <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

      ```
      nano device-role-trust-policy.json
      ```

      Copy the following JSON into the file.

      ```
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
              "Service": "credentials.iot.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
          }
        ]
      }
      ```

   1. Create the token exchange role with the trust policy document.
      + Replace {{GreengrassV2TokenExchangeRole}} with the name of the IAM role to create.

      ```
      aws iam create-role --role-name {{GreengrassV2TokenExchangeRole}} --assume-role-policy-document file://device-role-trust-policy.json
      ```

      The response looks similar to the following example, if the request succeeds.

      ```
      {
        "Role": {
          "Path": "/",
          "RoleName": "GreengrassV2TokenExchangeRole",
          "RoleId": "AROAZ2YMUHYHK5OKM77FB",
          "Arn": "arn:aws:iam::123456789012:role/GreengrassV2TokenExchangeRole",
          "CreateDate": "2021-02-06T00:13:29+00:00",
          "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
              {
                "Effect": "Allow",
                "Principal": {
                  "Service": "credentials.iot.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
              }
            ]
          }
        }
      ```

   1. Create a file that contains the access policy document that the token exchange role requires.

      <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

      ```
      nano device-role-access-policy.json
      ```

      Copy the following JSON into the file.

      ```
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "logs:CreateLogGroup",
              "logs:CreateLogStream",
              "logs:PutLogEvents",
              "logs:DescribeLogStreams",
              "s3:GetBucketLocation"
            ],
            "Resource": "*"
          }
        ]
      }
      ```
**Note**
This access policy doesn't allow access to component artifacts in S3 buckets. To deploy custom components that define artifacts in Amazon S3, you must add permissions to the role to allow your core device to retrieve component artifacts. For more information, see [Allow access to S3 buckets for component artifacts](device-service-role.md#device-service-role-access-s3-bucket).
If you don't yet have an S3 bucket for component artifacts, you can add these permissions later after you create a bucket.

   1. Create the IAM policy from the policy document.
      + Replace {{GreengrassV2TokenExchangeRoleAccess}} with the name of the IAM policy to create.

      ```
      aws iam create-policy --policy-name {{GreengrassV2TokenExchangeRoleAccess}} --policy-document file://device-role-access-policy.json
      ```

      The response looks similar to the following example, if the request succeeds.

      ```
      {
        "Policy": {
          "PolicyName": "GreengrassV2TokenExchangeRoleAccess",
          "PolicyId": "ANPAZ2YMUHYHACI7C5Z66",
          "Arn": "arn:aws:iam::123456789012:policy/GreengrassV2TokenExchangeRoleAccess",
          "Path": "/",
          "DefaultVersionId": "v1",
          "AttachmentCount": 0,
          "PermissionsBoundaryUsageCount": 0,
          "IsAttachable": true,
          "CreateDate": "2021-02-06T00:37:17+00:00",
          "UpdateDate": "2021-02-06T00:37:17+00:00"
        }
      }
      ```

   1. Attach the IAM policy to the token exchange role.
      + Replace {{GreengrassV2TokenExchangeRole}} with the name of the IAM role.
      + Replace the policy ARN with the ARN of the IAM policy that you created in the previous step.

      ```
      aws iam attach-role-policy --role-name {{GreengrassV2TokenExchangeRole}} --policy-arn {{arn:aws:iam::123456789012:policy/GreengrassV2TokenExchangeRoleAccess}}
      ```

      The command doesn't have any output if the request succeeds.

1. <a name="create-token-exchange-role-create-iot-role-alias"></a>Create an AWS IoT role alias that points to the token exchange role.
   + Replace {{GreengrassCoreTokenExchangeRoleAlias}} with the name of the role alias to create.
   + Replace the role ARN with the ARN of the IAM role that you created in the previous step.

   ```
   aws iot create-role-alias --role-alias {{GreengrassCoreTokenExchangeRoleAlias}} --role-arn {{arn:aws:iam::123456789012:role/GreengrassV2TokenExchangeRole}}
   ```

   The response looks similar to the following example, if the request succeeds.

   ```
   {
     "roleAlias": "GreengrassCoreTokenExchangeRoleAlias",
     "roleAliasArn": "arn:aws:iot:us-west-2:123456789012:rolealias/GreengrassCoreTokenExchangeRoleAlias"
   }
   ```
**Note**
To create a role alias, you must have permission to pass the token exchange IAM role to AWS IoT. If you receive an error message when you try to create a role alias, check that your AWS user has this permission. For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *AWS Identity and Access Management User Guide*.

1. Create and attach an AWS IoT policy that allows your Greengrass core device to use the role alias to assume the token exchange role. If you have set up a Greengrass core device before, you can attach its role alias AWS IoT policy instead of creating a new one. Do the following:

   1. (Optional) Create a file that contains the AWS IoT policy document that the role alias requires.

      <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

      ```
      nano greengrass-v2-iot-role-alias-policy.json
      ```

      Copy the following JSON into the file.
      + Replace the resource ARN with the ARN of your role alias.

      ```
      {
        "Version":"2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "iot:AssumeRoleWithCertificate",
            "Resource": "{{arn:aws:iot:us-west-2:123456789012:rolealias/GreengrassCoreTokenExchangeRoleAlias}}"
          }
        ]
      }
      ```

   1. Create an AWS IoT policy from the policy document.
      + Replace {{GreengrassCoreTokenExchangeRoleAliasPolicy}} with the name of the AWS IoT policy to create.

      ```
      aws iot create-policy --policy-name {{GreengrassCoreTokenExchangeRoleAliasPolicy}} --policy-document file://greengrass-v2-iot-role-alias-policy.json
      ```

      The response looks similar to the following example, if the request succeeds.

      ```
      {
        "policyName": "GreengrassCoreTokenExchangeRoleAliasPolicy",
        "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/GreengrassCoreTokenExchangeRoleAliasPolicy",
        "policyDocument": "{
          \\"Version\\":\\"2012-10-17		 	 	 \\",
          \\"Statement\\": [
            {
              \\"Effect\\": \\"Allow\\",
              \\"Action\\": \\"iot:AssumeRoleWithCertificate\\",
              \\"Resource\\": \\"arn:aws:iot:us-west-2:123456789012:rolealias/GreengrassCoreTokenExchangeRoleAlias\\"
            }
          ]
        }",
        "policyVersionId": "1"
      }
      ```

   1. Attach the AWS IoT policy to the AWS IoT thing's certificate.
      + Replace {{GreengrassCoreTokenExchangeRoleAliasPolicy}} with the name of the role alias AWS IoT policy.
      + Replace the target ARN with the ARN of the certificate for your AWS IoT thing.

      ```
      aws iot attach-policy --policy-name {{GreengrassCoreTokenExchangeRoleAliasPolicy}} --target {{arn:aws:iot:us-west-2:123456789012:cert/aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4}}
      ```

      The command doesn't have any output if the request succeeds.

### Download certificates to the device
<a name="download-thing-certificates"></a>

Earlier, you downloaded your device's certificate to your development computer. In this section, you copy the certificate to your core device to set up the device with the certificates that it uses to connect to AWS IoT. You also download the Amazon root certificate authority (CA) certificate. If you use an HSM, you also import the certificate file into the HSM in this section.
+ If you created the thing certificate and private key in the AWS IoT service earlier, follow the steps to download the certificates with private key and certificate files.
+ If you created the thing certificate from a private key in a hardware security module (HSM) earlier, follow the steps to download the certificates with the private key and certificate in an HSM.

#### Download certificates with private key and certificate files
<a name="download-thing-certificates-without-hardware-security"></a>

**To download certificates to the device**

1. <a name="installation-copy-thing-certificate-to-device"></a>Copy the AWS IoT thing certificate from your development computer to the device. If SSH and SCP are enabled on the development computer and the device, you can use the `scp` command on your development computer to transfer the certificate. Replace {{device-ip-address}} with the IP address of your device.

   ```
   scp -r greengrass-v2-certs/ {{device-ip-address}}:~
   ```

1. <a name="installation-create-greengrass-root-folder"></a>Create the Greengrass root folder on the device. You'll later install the AWS IoT Greengrass Core software to this folder.
**Note**
Windows has a path length limitation of 260 characters. If you are using Windows, use a root folder like `C:\greengrass\v2` or `D:\greengrass\v2` to keep the Greengrass components paths under the 260 character limit.

------
#### [ Linux or Unix ]
   + Replace `{{/greengrass/v2}}` with the folder to use.

   ```
   sudo mkdir -p {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   mkdir {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   mkdir {{C:\greengrass\v2}}
   ```

------

1. <a name="installation-set-greengrass-root-folder-permissions"></a>(Linux only) Set the permissions of the parent of the Greengrass root folder.
   + Replace {{/greengrass}} with the parent of the root folder.

   ```
   sudo chmod 755 {{/greengrass}}
   ```

1. Copy the AWS IoT thing certificates to the Greengrass root folder.

------
#### [ Linux or Unix ]
   + Replace `{{/greengrass/v2}}` with the Greengrass root folder.

   ```
   sudo cp -R ~/greengrass-v2-certs/* {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   robocopy %USERPROFILE%\greengrass-v2-certs {{C:\greengrass\v2}} /E
   ```

------
#### [ PowerShell ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   cp -Path ~\greengrass-v2-certs\* -Destination {{C:\greengrass\v2}}
   ```

------

1. Download the Amazon root certificate authority (CA) certificate. AWS IoT certificates are associated with Amazon's root CA certificate by default. Download the CA1 certificate and the [CA3 certificate](https://www.amazontrust.com/repository/).

------
#### [ Linux or Unix ]
   + Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the Greengrass root folder.

   ```
   sudo curl -o {{/greengrass/v2}}/AmazonRootCA1.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
   sudo curl -o - https://www.amazontrust.com/repository/AmazonRootCA3.pem >> {{/greengrass/v2}}/AmazonRootCA1.pem
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -o {{C:\greengrass\v2}}\\AmazonRootCA1.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://www.amazontrust.com/repository/AmazonRootCA1.pem -OutFile {{C:\greengrass\v2}}\\AmazonRootCA1.pem
   ```

------

#### Download certificates with the private key and certificate in an HSM
<a name="download-thing-certificates-with-hardware-security"></a>

**Note**
This feature is available for v2.5.3 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md). AWS IoT Greengrass doesn't currently support this feature on Windows core devices.

**To download certificates to the device**

1. <a name="installation-copy-thing-certificate-to-device"></a>Copy the AWS IoT thing certificate from your development computer to the device. If SSH and SCP are enabled on the development computer and the device, you can use the `scp` command on your development computer to transfer the certificate. Replace {{device-ip-address}} with the IP address of your device.

   ```
   scp -r greengrass-v2-certs/ {{device-ip-address}}:~
   ```

1. <a name="installation-create-greengrass-root-folder"></a>Create the Greengrass root folder on the device. You'll later install the AWS IoT Greengrass Core software to this folder.
**Note**
Windows has a path length limitation of 260 characters. If you are using Windows, use a root folder like `C:\greengrass\v2` or `D:\greengrass\v2` to keep the Greengrass components paths under the 260 character limit.

------
#### [ Linux or Unix ]
   + Replace `{{/greengrass/v2}}` with the folder to use.

   ```
   sudo mkdir -p {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   mkdir {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   mkdir {{C:\greengrass\v2}}
   ```

------

1. <a name="installation-set-greengrass-root-folder-permissions"></a>(Linux only) Set the permissions of the parent of the Greengrass root folder.
   + Replace {{/greengrass}} with the parent of the root folder.

   ```
   sudo chmod 755 {{/greengrass}}
   ```

1. Import the thing certificate file, `~/greengrass-v2-certs/device.pem.crt`, into the HSM. Check the documentation for your HSM to learn how to import certificates into it. Import the certificate using the same token, slot ID, user PIN, object label, and object ID (if your HSM uses one) where you generated the private key in the HSM earlier.
**Note**
If you generated the private key earlier without an object ID, and the certificate has an object ID, set the private key's object ID to the same value as the certificate. Check the documentation for your HSM to learn how to set the object ID for the private key object.

1. (Optional) Delete the thing certificate file, so that it exists only in the HSM.

   ```
   rm ~/greengrass-v2-certs/device.pem.crt
   ```

1. Download the Amazon root certificate authority (CA) certificate. AWS IoT certificates are associated with Amazon's root CA certificate by default. Download both the CA1 and the [CA3 certificate](https://www.amazontrust.com/repository/).

------
#### [ Linux or Unix ]
   + Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the Greengrass root folder.

   ```
   sudo curl -o {{/greengrass/v2}}/AmazonRootCA1.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
   sudo curl -o - https://www.amazontrust.com/repository/AmazonRootCA3.pem >> {{/greengrass/v2}}/AmazonRootCA1.pem
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -o {{C:\greengrass\v2}}\\AmazonRootCA1.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://www.amazontrust.com/repository/AmazonRootCA1.pem -OutFile {{C:\greengrass\v2}}\\AmazonRootCA1.pem
   ```

------

### Set up the device environment
<a name="set-up-device-environment"></a>

Follow the steps in this section to set up a Linux or Windows device to use as your AWS IoT Greengrass core device.

#### Set up a Linux device
<a name="set-up-linux-device-environment"></a><a name="set-up-linux-device-environment-procedure"></a>

**To set up a Linux device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required. The following commands show you how to install OpenJDK on your device.
   + For Debian-based or Ubuntu-based distributions:

     ```
     sudo apt install default-jdk
     ```
   + For Red Hat-based distributions:

     ```
     sudo yum install java-11-openjdk-devel
     ```
   + For Amazon Linux 2:

     ```
     sudo amazon-linux-extras install java-openjdk11
     ```
   + For Amazon Linux 2023:

     ```
     sudo dnf install java-11-amazon-corretto -y
     ```

   When the installation completes, run the following command to verify that Java runs on your Linux device.

   ```
   java -version
   ```

   The command prints the version of Java that runs on the device. For example, on a Debian-based distribution, the output might look similar to the following sample.

   ```
   openjdk version "11.0.9.1" 2020-11-04
   OpenJDK Runtime Environment (build 11.0.9.1+1-post-Debian-1deb10u2)
   OpenJDK 64-Bit Server VM (build 11.0.9.1+1-post-Debian-1deb10u2, mixed mode)
   ```

1. (Optional) Create the default system user and group that runs components on the device. You can also choose to let the AWS IoT Greengrass Core software installer create this user and group during installation with the `--component-default-user` installer argument. For more information, see [Installer arguments](configure-installer.md).

   ```
   sudo useradd --system --create-home ggc_user
   sudo groupadd --system ggc_group
   ```

1. Verify that the user that runs the AWS IoT Greengrass Core software (typically `root`), has permission to run `sudo` with any user and any group.

   1. Run the following command to open the `/etc/sudoers` file.

      ```
      sudo visudo
      ```

   1. Verify that the permission for the user looks like the following example.

      ```
      root    ALL=(ALL:ALL) ALL
      ```

1. (Optional) To [run containerized Lambda functions](run-lambda-functions.md), you must enable [cgroups](https://en.wikipedia.org/wiki/Cgroups) v1, and you must enable and mount the *memory* and *devices* cgroups. If you don't plan to run containerized Lambda functions, you can skip this step.

   To enable these cgroups options, boot the device with the following Linux kernel parameters.

   ```
   cgroup_enable=memory cgroup_memory=1 systemd.unified_cgroup_hierarchy=0
   ```

   For information about viewing and setting kernel parameters for your device, see the documentation for your operating system and boot loader. Follow the instructions to permanently set the kernel parameters.

1. Install all other required dependencies on your device as indicated by the list of requirements in [Device requirements](greengrass-nucleus-component.md#greengrass-v2-requirements).

#### Set up a Windows device
<a name="set-up-windows-device-environment"></a>

**Note**
This feature is available for v2.5.0 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md).<a name="set-up-windows-device-environment-procedure"></a>

**To set up a Windows device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required.

1. Check whether Java is available on the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) system variable, and add it if not. The LocalSystem account runs the AWS IoT Greengrass Core software, so you must add Java to the PATH system variable instead of the PATH user variable for your user. Do the following:

   1. Press the Windows key to open the start menu.

   1. Type **environment variables** to search for the system options from the start menu.

   1. In the start menu search results, choose **Edit the system environment variables** to open the **System properties** window.

   1. Choose **Environment variables...** to open the **Environment Variables** window.

   1. Under **System variables**, select **Path**, and then choose **Edit**. In the **Edit environment variable** window, you can view each path on a separate line.

   1. Check if the path to the Java installation's `bin` folder is present. The path might look similar to the following example.

      ```
      C:\\Program Files\\Amazon Corretto\\jdk11.0.13_8\\bin
      ```

   1. If the Java installation's `bin` folder is missing from **Path**, choose **New** to add it, and then choose **OK**.

1. <a name="set-up-windows-device-environment-open-cmd"></a>Open the Windows Command Prompt (`cmd.exe`) as an administrator.

1. <a name="set-up-windows-device-environment-create"></a>Create the default user in the LocalSystem account on the Windows device. Replace {{password}} with a secure password.

   ```
   net user /add ggc_user {{password}}
   ```
**Tip**  <a name="windows-password-expiration-tip"></a>
Depending on your Windows configuration, the user's password might be set to expire at a date in the future. To ensure your Greengrass applications continue to operate, track when the password expires, and update it before it expires. You can also set the user's password to never expire.
To check when a user and its password expire, run the following command.

     ```
     net user {{ggc_user}} | findstr /C:expires
     ```
To set a user's password to never expire, run the following command.

     ```
     wmic UserAccount where "Name='{{ggc_user}}'" set PasswordExpires=False
     ```
If you’re using Windows 10 or later where the [`wmic` command is deprecated](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic), run the following PowerShell command.

     ```
     Get-CimInstance -Query "SELECT * from Win32_UserAccount WHERE name = '{{ggc_user}}'" | Set-CimInstance -Property @{PasswordExpires="False"}
     ```

1. <a name="set-up-windows-device-psexec"></a>Download and install the [PsExec utility](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) from Microsoft on the device.

1. <a name="set-up-windows-device-credentials"></a>Use the PsExec utility to store the user name and password for the default user in the Credential Manager instance for the LocalSystem account. Replace {{password}} with the user's password that you set earlier.

   ```
   psexec -s cmd /c cmdkey /generic:ggc_user /user:ggc_user /pass:{{password}}
   ```

   If the **PsExec License Agreement** opens, choose **Accept** to agree to the license and run the command.
**Note**
On Windows devices, the LocalSystem account runs the Greengrass nucleus, and you must use the PsExec utility to store the default user information in the LocalSystem account. Using the Credential Manager application stores this information in the Windows account of the currently logged on user, instead of the LocalSystem account.

### Download the AWS IoT Greengrass Core software
<a name="download-greengrass-core-v2"></a>

You can download the latest version of the AWS IoT Greengrass Core software from the following location:
+ [https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip](https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip)

**Note**
You can download a specific version of the AWS IoT Greengrass Core software from the following location. Replace {{version}} with the version to download.

```
https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-{{version}}.zip
```

**To download the AWS IoT Greengrass Core software**

1. <a name="installation-download-ggc-software-step"></a>On your core device, download the AWS IoT Greengrass Core software to a file named `greengrass-nucleus-latest.zip`.

------
#### [ Linux or Unix ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip -OutFile greengrass-nucleus-latest.zip
   ```

------

   <a name="core-software-license"></a>By downloading this software, you agree to the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

1. <a name="verify-gg-nucleus-signature"></a>(Optional) To verify the Greengrass nucleus software signature
**Note**
This feature is available with Greengrass nucleus version 2.9.5 and later.

   1. Use the following command to verify your Greengrass nucleus artifact's signature:

------
#### [ Linux or Unix ]

      ```
      jarsigner -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------
#### [ Windows Command Prompt (CMD) ]

      The file name might look different depending on the JDK version you install. Replace {{`jdk17.0.6_10`}} with the JDK version you installed.

      ```
      "C:\\Program Files\\Amazon Corretto\\{{jdk17.0.6_10}}\\bin\\jarsigner.exe" -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------
#### [ PowerShell ]

      The file name might look different depending on the JDK version you install. Replace {{`jdk17.0.6_10`}} with the JDK version you installed.

      ```
      'C:\\Program Files\\Amazon Corretto\\{{jdk17.0.6_10}}\\bin\\jarsigner.exe' -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------

   1. The `jarsigner` invocation yields output that indicates the results of the verification.

      1. If the Greengrass nucleus zip file is signed, the output contains the following statement:

         ```
         jar verified.
         ```

      1. If the Greengrass nucleus zip file isn't signed, the output contains the following statement:

         ```
         jar is unsigned.
         ```

   1. If you provided the Jarsigner `-certs` option along with `-verify` and `-verbose` options, the output also includes detailed signer certificate information.

1. <a name="installation-unzip-ggc-software-step"></a>Unzip the AWS IoT Greengrass Core software to a folder on your device. Replace {{GreengrassInstaller}} with the folder that you want to use.

------
#### [ Linux or Unix ]

   ```
   unzip greengrass-nucleus-latest.zip -d {{GreengrassInstaller}} && rm greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   mkdir {{GreengrassInstaller}} && tar -xf greengrass-nucleus-latest.zip -C {{GreengrassInstaller}} && del greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   Expand-Archive -Path greengrass-nucleus-latest.zip -DestinationPath .\\{{GreengrassInstaller}}
   rm greengrass-nucleus-latest.zip
   ```

------

1. (Optional) Run the following command to see the version of the AWS IoT Greengrass Core software.

   ```
   java -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar --version
   ```

**Important**  <a name="installer-folder-2.4.0-warning"></a>
If you install a version of the Greengrass nucleus earlier than v2.4.0, don't remove this folder after you install the AWS IoT Greengrass Core software. The AWS IoT Greengrass Core software uses the files in this folder to run.
If you downloaded the latest version of the software, you install v2.4.0 or later, and you can remove this folder after you install the AWS IoT Greengrass Core software.

### Install the AWS IoT Greengrass Core software
<a name="run-greengrass-core-v2-installer-manual-fips"></a>

Run the installer with arguments that specify the following actions:
+ Install from a partial configuration file that specifies to use the AWS resources and certificates that you created earlier. The AWS IoT Greengrass Core software uses a configuration file that specifies the configuration of every Greengrass component on the device. The installer creates a complete configuration file from the partial configuration file that you provide.
+ <a name="install-argument-component-default-user"></a>Specify to use the `ggc_user` system user to run software components on the core device. On Linux devices, this command also specifies to use the `ggc_group` system group, and the installer creates the system user and group for you.
+ <a name="install-argument-system-service"></a>Set up the AWS IoT Greengrass Core software as a system service that runs at boot. On Linux devices, this requires the [Systemd](https://en.wikipedia.org/wiki/Systemd) init system.
**Important**  <a name="windows-system-service-requirement-important-note"></a>
On Windows core devices, you must set up the AWS IoT Greengrass Core software as a system service.

For more information about the arguments that you can specify, see [Installer arguments](configure-installer.md).

**Note**
<a name="jvm-tuning-note"></a>If you are running AWS IoT Greengrass on a device with limited memory, you can control the amount of memory that AWS IoT Greengrass Core software uses. To control memory allocation, you can set JVM heap size options in the `jvmOptions` configuration parameter in your nucleus component. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).
+ If you created the thing certificate and private key in the AWS IoT service earlier, follow the steps to install the AWS IoT Greengrass Core software with private key and certificate files.
+ If you created the thing certificate from a private key in a hardware security module (HSM) earlier, follow the steps to install the AWS IoT Greengrass Core software with the private key and certificate in an HSM.

#### Install the AWS IoT Greengrass Core software with private key and certificate files
<a name="FIPS-manual-installation-without-hardware-security"></a>

**To install the AWS IoT Greengrass Core software**

1. <a name="installer-check-greengrass-core-software-version"></a>Check the version of the AWS IoT Greengrass Core software.
   + Replace {{GreengrassInstaller}} with the path to the folder that contains the software.

   ```
   java -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar --version
   ```

1. Use a text editor to create a configuration file named `config.yaml` to provide to the installer.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano {{GreengrassInstaller}}/config.yaml
   ```

   Copy the following YAML content into the file. This partial configuration file specifies system parameters and Greengrass nucleus parameters.

   ```
   ---
   system:
     certificateFilePath: "{{/greengrass/v2}}/device.pem.crt"
     privateKeyPath: "{{/greengrass/v2}}/private.pem.key"
     rootCaPath: "{{/greengrass/v2}}/AmazonRootCA1.pem"
     rootpath: "{{/greengrass/v2}}"
     thingName: "{{MyGreengrassCore}}"
   services:
     aws.greengrass.Nucleus:
       componentType: "NUCLEUS"
       version: "{{2.18.0}}"
       configuration:
         awsRegion: "{{us-west-2}}"
         iotRoleAlias: "{{GreengrassCoreTokenExchangeRoleAlias}}"
         fipsMode: "true"
         iotDataEndpoint: "{{data.iot-fips.us-west-2.amazonaws.com}}"
         greengrassDataPlaneEndpoint: "iotData"
         iotCredEndpoint: "{{data.credentials.iot-fips.us-west-2.amazonaws.com}}"
   ```

   Then, do the following:
   + Replace each instance of `{{/greengrass/v2}}` with the Greengrass root folder.
   + Replace {{MyGreengrassCore}} with the name of the AWS IoT thing.
   + Replace {{2.18.0}} with the version of the AWS IoT Greengrass Core software.
   + Replace {{us-west-2}} with the AWS Region where you created the resources.
   + Replace {{GreengrassCoreTokenExchangeRoleAlias}} with the name of the token exchange role alias.
   + Replace the {{iotDataEndpoint}} with your AWS IoT data endpoint.
   + Replace the {{iotCredEndpoint}} with your AWS IoT credentials endpoint.

1. Run the installer, and specify `--init-config` to provide the configuration file.
   + Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the Greengrass root folder.
   + Replace each instance of {{GreengrassInstaller}} with the folder where you unpacked the installer.

------
#### [ Linux or Unix ]

   ```
   sudo -E java -Droot="{{/greengrass/v2}}" -Dlog.store=FILE \
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar \
     --init-config ./{{GreengrassInstaller}}/config.yaml \
     --component-default-user ggc_user:ggc_group \
     --setup-system-service true
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" ^
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar ^
     --init-config ./{{GreengrassInstaller}}/config.yaml ^
     --component-default-user ggc_user ^
     --setup-system-service true
   ```

------
#### [ PowerShell ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" `
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar `
     --init-config ./{{GreengrassInstaller}}/config.yaml `
     --component-default-user ggc_user `
     --setup-system-service true
   ```

------
**Important**  <a name="windows-system-service-installer-argument-important-note"></a>
On Windows core devices, you must specify `--setup-system-service true` to set up the AWS IoT Greengrass Core software as a system service.

   <a name="installer-setup-system-service-output-message"></a>If you specify `--setup-system-service true`, the installer prints `Successfully set up Nucleus as a system service` if it set up and ran the software as a system service. Otherwise, the installer doesn't output any message if it installs the software successfully.
**Note**  <a name="installer-deploy-dev-tools-without-provision"></a>
You can't use the `deploy-dev-tools` argument to deploy local development tools when you run the installer without the `--provision true` argument. For information about deploying the Greengrass CLI directly on your device, see [Greengrass Command Line Interface](gg-cli.md).

1. <a name="installer-verify-installation"></a>Verify the installation by viewing the files in the root folder.

------
#### [ Linux or Unix ]

   ```
   ls {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   dir {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]

   ```
   ls {{C:\greengrass\v2}}
   ```

------

   If the installation succeeded, the root folder contains several folders, such as `config`, `packages`, and `logs`.

#### Install the AWS IoT Greengrass Core software with the private key and certificate in an HSM
<a name="FIPS-manual-installation-with-hardware-security"></a>

**Note**
This feature is available for v2.5.3 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md). AWS IoT Greengrass doesn't currently support this feature on Windows core devices.

**To install the AWS IoT Greengrass Core software**

1. <a name="installer-check-greengrass-core-software-version"></a>Check the version of the AWS IoT Greengrass Core software.
   + Replace {{GreengrassInstaller}} with the path to the folder that contains the software.

   ```
   java -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar --version
   ```

1. To enable the AWS IoT Greengrass Core software to use the private key and certificate in the HSM, install the [PKCS\#11 provider component](pkcs11-provider-component.md) when you install the AWS IoT Greengrass Core software. The PKCS\#11 provider component is a plugin that you can configure during installation. You can download the latest version of the PKCS\#11 provider component from the following location:
   + [https://d2s8p88vqu9w66.cloudfront.net/releases/Pkcs11Provider/aws.greengrass.crypto.Pkcs11Provider-latest.jar](https://d2s8p88vqu9w66.cloudfront.net/releases/Pkcs11Provider/aws.greengrass.crypto.Pkcs11Provider-latest.jar)

   Download the PKCS\#11 provider plugin to a file named `aws.greengrass.crypto.Pkcs11Provider.jar`. Replace {{GreengrassInstaller}} with the folder that you want to use.

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/Pkcs11Provider/aws.greengrass.crypto.Pkcs11Provider-latest.jar > {{GreengrassInstaller}}/aws.greengrass.crypto.Pkcs11Provider.jar
   ```

   <a name="core-software-license"></a>By downloading this software, you agree to the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

1. Use a text editor to create a configuration file named `config.yaml` to provide to the installer.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano {{GreengrassInstaller}}/config.yaml
   ```

   Copy the following YAML content into the file. This partial configuration file specifies system parameters, Greengrass nucleus parameters, and PKCS\#11 provider parameters.

   ```
   ---
   system:
     certificateFilePath: "{{/greengrass/v2}}/device.pem.crt"
     privateKeyPath: "{{/greengrass/v2}}/private.pem.key"
     rootCaPath: "{{/greengrass/v2}}/AmazonRootCA1.pem"
     rootpath: "{{/greengrass/v2}}"
     thingName: "{{MyGreengrassCore}}"
   services:
     aws.greengrass.Nucleus:
       componentType: "NUCLEUS"
       version: "{{2.18.0}}"
       configuration:
         awsRegion: "{{us-west-2}}"
         iotRoleAlias: "{{GreengrassCoreTokenExchangeRoleAlias}}"
         fipsMode: "true"
         iotDataEndpoint: "{{data.iot-fips.us-west-2.amazonaws.com}}"
         greengrassDataPlaneEndpoint: "iotData"
         iotCredEndpoint: "{{data.credentials.iot-fips.us-west-2.amazonaws.com}}"
   ```

   Then, do the following:
   + Replace each instance of {{iotdevicekey}} in the PKCS\#11 URIs with the object label where you created the private key and imported the certificate.
   + Replace each instance of `{{/greengrass/v2}}` with the Greengrass root folder.
   + Replace {{MyGreengrassCore}} with the name of the AWS IoT thing.
   + Replace {{2.18.0}} with the version of the AWS IoT Greengrass Core software.
   + Replace {{us-west-2}} with the AWS Region where you created the resources.
   + Replace {{GreengrassCoreTokenExchangeRoleAlias}} with the name of the token exchange role alias.
   + Replace the `iotDataEndpoint` with your AWS IoT data endpoint.
   + Replace the `iotCredEndpoint` with your AWS IoT credentials endpoint.
   + Replace the configuration parameters for the `aws.greengrass.crypto.Pkcs11Provider` component with the values for the HSM configuration on the core device.

1. Run the installer, and specify `--init-config` to provide the configuration file.
   + Replace `{{/greengrass/v2}}` with the Greengrass root folder.
   + Replace each instance of {{GreengrassInstaller}} with the folder where you unpacked the installer.

   ```
   sudo -E java -Droot="{{/greengrass/v2}}" -Dlog.store=FILE \
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar \
     --trusted-plugin ./{{GreengrassInstaller}}/aws.greengrass.crypto.Pkcs11Provider.jar \
     --init-config ./{{GreengrassInstaller}}/config.yaml \
     --component-default-user ggc_user:ggc_group \
     --setup-system-service true
   ```
**Important**  <a name="windows-system-service-installer-argument-important-note"></a>
On Windows core devices, you must specify `--setup-system-service true` to set up the AWS IoT Greengrass Core software as a system service.

   <a name="installer-setup-system-service-output-message"></a>If you specify `--setup-system-service true`, the installer prints `Successfully set up Nucleus as a system service` if it set up and ran the software as a system service. Otherwise, the installer doesn't output any message if it installs the software successfully.
**Note**  <a name="installer-deploy-dev-tools-without-provision"></a>
You can't use the `deploy-dev-tools` argument to deploy local development tools when you run the installer without the `--provision true` argument. For information about deploying the Greengrass CLI directly on your device, see [Greengrass Command Line Interface](gg-cli.md).

1. <a name="installer-verify-installation"></a>Verify the installation by viewing the files in the root folder.

------
#### [ Linux or Unix ]

   ```
   ls {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   dir {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]

   ```
   ls {{C:\greengrass\v2}}
   ```

------

   If the installation succeeded, the root folder contains several folders, such as `config`, `packages`, and `logs`.

<a name="install-greengrass-core-run-software"></a>If you installed the AWS IoT Greengrass Core software as a system service, the installer runs the software for you. Otherwise, you must run the software manually. For more information, see [Run the AWS IoT Greengrass Core software](run-greengrass-core-v2.md).

<a name="install-greengrass-core-next-steps-intro"></a>For more information about how to configure and use the software and AWS IoT Greengrass, see the following:<a name="install-greengrass-core-next-steps-links"></a>
+ [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md)
+ [Develop AWS IoT Greengrass components](develop-greengrass-components.md)
+ [Deploy AWS IoT Greengrass components to devices](manage-deployments.md)
+ [Greengrass Command Line Interface](gg-cli.md)

## Install FIPS endpoints with fleet provisioning
<a name="FIPS-fleet-provisioning"></a>

This feature is available for v2.4.0 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md).

Install FIPS endpoints on your AWS IoT Greengrass Core software with AWS IoT fleet provisioning for your core devices.

**Note**
The fleet provisioning plugin for [Greengrass nucleus](greengrass-nucleus-component.md) doesn't currently support storing private key and certificate files in a hardware security module (HSM). To use an HSM, [install the AWS IoT Greengrass Core software with manual provisioning](#FIPS-fleet-provisioning).

To install the AWS IoT Greengrass Core software with AWS IoT fleet provisioning, you must set up resources in your AWS account that AWS IoT uses to provision Greengrass core devices. These resources include a provisioning template, claim certificates, and a [token exchange IAM role](device-service-role.md). After you create these resources, you can reuse them to provision multiple core devices in a fleet. For more information, see [Set up AWS IoT fleet provisioning for Greengrass core devices](fleet-provisioning-setup.md).

**Important**  <a name="install-greengrass-core-requirements-note"></a>
Before you download the AWS IoT Greengrass Core software, check that your core device meets the [requirements](greengrass-nucleus-component.md#greengrass-v2-requirements) to install and run the AWS IoT Greengrass Core software v2.0.

**Topics**
+ [Prerequisites](#fleet-provisioning-prerequisites)
+ [Retrieve AWS IoT endpoints](#retrieve-iot-endpoints)
+ [Download certificates to the device](#download-claim-certificates)
+ [Set up the device environment](#set-up-device-environment-fleet-provisioning)
+ [Download the AWS IoT Greengrass Core software](#download-greengrass-core-v2-fleet)
+ [Download the AWS IoT fleet provisioning plugin](#download-fleet-provisioning-plugin)
+ [Install the AWS IoT Greengrass Core software](#run-greengrass-core-v2-installer-fleet-provisioning)

### Prerequisites
<a name="fleet-provisioning-prerequisites"></a>

To install the AWS IoT Greengrass Core software with AWS IoT fleet provisioning, you must first [set up AWS IoT fleet provisioning for Greengrass core devices](fleet-provisioning-setup.md). After you complete these steps once, you can use fleet provisioning to install the AWS IoT Greengrass Core software on any number of devices.

### Retrieve AWS IoT endpoints
<a name="retrieve-iot-endpoints"></a>

Get the FIPS endpoints for your AWS account, and save them to use later. Your device uses these endpoints to connect to AWS IoT. Do the following:

1. Get the FIPS data endpoint for your region in the [AWS IoT Core FIPS data plane endpoints.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints) The FIPS data endpoint for your AWS account should look like this: {{data.iot-fips.us-west-2.amazonaws.com}}

1. Get the FIPS credentials endpoint for your region in the [AWS IoT Core FIPS data plane endpoints.](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints) The FIPS credentials endpoint for your AWS account should look like this: {{data.credentials.iot-fips.us-west-2.amazonaws.com}}

### Download certificates to the device
<a name="download-claim-certificates"></a>

The device uses a claim certificate and private key to authenticate its request to provision AWS resources and acquire an X.509 device certificate. You can embed the claim certificate and private key into the device during manufacturing, or copy the certificate and key to the device during installation. In this section, you copy the claim certificate and private key to the device. You also download the Amazon Root certificate authority (CA) certificate to the device.

**Important**  <a name="installation-fleet-provisioning-secure-claim-private-keys"></a>
Provisioning claim private keys should be secured at all times, including on Greengrass core devices. We recommend that you use Amazon CloudWatch metrics and logs to monitor for indications of misuse, such as unauthorized use of the claim certificate to provision devices. If you detect misuse, disable the provisioning claim certificate so that it can't be used for device provisioning. For more information, see [Monitoring AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html) in the *AWS IoT Core Developer Guide*.
To help you better manage the number of devices, and which devices, that register themselves in your AWS account, you can specify a pre-provisioning hook when you create a fleet provisioning template. A pre-provisioning hook is an AWS Lambda function that validates template parameters that devices provide during registration. For example, you might create a pre-provisioning hook that checks a device ID against a database to verify that the device has permission to provision. For more information, see [Pre-provisioning hooks](https://docs.aws.amazon.com/iot/latest/developerguide/pre-provisioning-hook.html) in the *AWS IoT Core Developer Guide*.

**To download claim certificates to the device**

1. Copy the claim certificate and private key to the device. If SSH and SCP are enabled on the development computer and the device, you can use the `scp` command on your development computer to transfer the claim certificate and private key. The following example command transfers these files a folder named `claim-certs` on your development computer to the device. Replace {{device-ip-address}} with the IP address of your device.

   ```
   scp -r claim-certs/ {{device-ip-address}}:~
   ```

1. <a name="installation-create-greengrass-root-folder"></a>Create the Greengrass root folder on the device. You'll later install the AWS IoT Greengrass Core software to this folder.
**Note**
Windows has a path length limitation of 260 characters. If you are using Windows, use a root folder like `C:\greengrass\v2` or `D:\greengrass\v2` to keep the Greengrass components paths under the 260 character limit.

------
#### [ Linux or Unix ]
   + Replace `{{/greengrass/v2}}` with the folder to use.

   ```
   sudo mkdir -p {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   mkdir {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]
   + Replace {{C:\\greengrass\\v2}} with the folder to use.

   ```
   mkdir {{C:\greengrass\v2}}
   ```

------

1. <a name="installation-set-greengrass-root-folder-permissions"></a>(Linux only) Set the permissions of the parent of the Greengrass root folder.
   + Replace {{/greengrass}} with the parent of the root folder.

   ```
   sudo chmod 755 {{/greengrass}}
   ```

1. Move the claim certificates to the Greengrass root folder.
   + Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the Greengrass root folder.

------
#### [ Linux or Unix ]

   ```
   sudo mv ~/claim-certs {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   move %USERPROFILE%\claim-certs {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]

   ```
   mv -Path ~\claim-certs -Destination {{C:\greengrass\v2}}
   ```

------

1. Download both the CA1 certificate and the [CA3 certificate](https://www.amazontrust.com/repository/).

------
#### [ Linux or Unix ]

   ```
   sudo curl -o - https://www.amazontrust.com/repository/AmazonRootCA3.pem >> {{/greengrass/v2}}/AmazonRootCA1.pem
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -o {{C:\greengrass\v2}}\\AmazonRootCA1.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://www.amazontrust.com/repository/AmazonRootCA1.pem -OutFile {{C:\greengrass\v2}}\\AmazonRootCA1.pem
   ```

------

### Set up the device environment
<a name="set-up-device-environment-fleet-provisioning"></a>

Follow the steps in this section to set up a Linux or Windows device to use as your AWS IoT Greengrass core device.

#### Set up a Linux device
<a name="set-up-linux-device-environment-fleet-provisioning"></a><a name="set-up-linux-device-environment-procedure"></a>

**To set up a Linux device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required. The following commands show you how to install OpenJDK on your device.
   + For Debian-based or Ubuntu-based distributions:

     ```
     sudo apt install default-jdk
     ```
   + For Red Hat-based distributions:

     ```
     sudo yum install java-11-openjdk-devel
     ```
   + For Amazon Linux 2:

     ```
     sudo amazon-linux-extras install java-openjdk11
     ```
   + For Amazon Linux 2023:

     ```
     sudo dnf install java-11-amazon-corretto -y
     ```

   When the installation completes, run the following command to verify that Java runs on your Linux device.

   ```
   java -version
   ```

   The command prints the version of Java that runs on the device. For example, on a Debian-based distribution, the output might look similar to the following sample.

   ```
   openjdk version "11.0.9.1" 2020-11-04
   OpenJDK Runtime Environment (build 11.0.9.1+1-post-Debian-1deb10u2)
   OpenJDK 64-Bit Server VM (build 11.0.9.1+1-post-Debian-1deb10u2, mixed mode)
   ```

1. (Optional) Create the default system user and group that runs components on the device. You can also choose to let the AWS IoT Greengrass Core software installer create this user and group during installation with the `--component-default-user` installer argument. For more information, see [Installer arguments](configure-installer.md).

   ```
   sudo useradd --system --create-home ggc_user
   sudo groupadd --system ggc_group
   ```

1. Verify that the user that runs the AWS IoT Greengrass Core software (typically `root`), has permission to run `sudo` with any user and any group.

   1. Run the following command to open the `/etc/sudoers` file.

      ```
      sudo visudo
      ```

   1. Verify that the permission for the user looks like the following example.

      ```
      root    ALL=(ALL:ALL) ALL
      ```

1. (Optional) To [run containerized Lambda functions](run-lambda-functions.md), you must enable [cgroups](https://en.wikipedia.org/wiki/Cgroups) v1, and you must enable and mount the *memory* and *devices* cgroups. If you don't plan to run containerized Lambda functions, you can skip this step.

   To enable these cgroups options, boot the device with the following Linux kernel parameters.

   ```
   cgroup_enable=memory cgroup_memory=1 systemd.unified_cgroup_hierarchy=0
   ```

   For information about viewing and setting kernel parameters for your device, see the documentation for your operating system and boot loader. Follow the instructions to permanently set the kernel parameters.

1. Install all other required dependencies on your device as indicated by the list of requirements in [Device requirements](greengrass-nucleus-component.md#greengrass-v2-requirements).

#### Set up a Windows device
<a name="set-up-windows-device-environment-fleet-provisioning"></a>

**Note**
This feature is available for v2.5.0 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md).<a name="set-up-windows-device-environment-procedure"></a>

**To set up a Windows device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required.

1. Check whether Java is available on the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) system variable, and add it if not. The LocalSystem account runs the AWS IoT Greengrass Core software, so you must add Java to the PATH system variable instead of the PATH user variable for your user. Do the following:

   1. Press the Windows key to open the start menu.

   1. Type **environment variables** to search for the system options from the start menu.

   1. In the start menu search results, choose **Edit the system environment variables** to open the **System properties** window.

   1. Choose **Environment variables...** to open the **Environment Variables** window.

   1. Under **System variables**, select **Path**, and then choose **Edit**. In the **Edit environment variable** window, you can view each path on a separate line.

   1. Check if the path to the Java installation's `bin` folder is present. The path might look similar to the following example.

      ```
      C:\\Program Files\\Amazon Corretto\\jdk11.0.13_8\\bin
      ```

   1. If the Java installation's `bin` folder is missing from **Path**, choose **New** to add it, and then choose **OK**.

1. <a name="set-up-windows-device-environment-open-cmd"></a>Open the Windows Command Prompt (`cmd.exe`) as an administrator.

1. <a name="set-up-windows-device-environment-create"></a>Create the default user in the LocalSystem account on the Windows device. Replace {{password}} with a secure password.

   ```
   net user /add ggc_user {{password}}
   ```
**Tip**  <a name="windows-password-expiration-tip"></a>
Depending on your Windows configuration, the user's password might be set to expire at a date in the future. To ensure your Greengrass applications continue to operate, track when the password expires, and update it before it expires. You can also set the user's password to never expire.
To check when a user and its password expire, run the following command.

     ```
     net user {{ggc_user}} | findstr /C:expires
     ```
To set a user's password to never expire, run the following command.

     ```
     wmic UserAccount where "Name='{{ggc_user}}'" set PasswordExpires=False
     ```
If you’re using Windows 10 or later where the [`wmic` command is deprecated](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic), run the following PowerShell command.

     ```
     Get-CimInstance -Query "SELECT * from Win32_UserAccount WHERE name = '{{ggc_user}}'" | Set-CimInstance -Property @{PasswordExpires="False"}
     ```

1. <a name="set-up-windows-device-psexec"></a>Download and install the [PsExec utility](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) from Microsoft on the device.

1. <a name="set-up-windows-device-credentials"></a>Use the PsExec utility to store the user name and password for the default user in the Credential Manager instance for the LocalSystem account. Replace {{password}} with the user's password that you set earlier.

   ```
   psexec -s cmd /c cmdkey /generic:ggc_user /user:ggc_user /pass:{{password}}
   ```

   If the **PsExec License Agreement** opens, choose **Accept** to agree to the license and run the command.
**Note**
On Windows devices, the LocalSystem account runs the Greengrass nucleus, and you must use the PsExec utility to store the default user information in the LocalSystem account. Using the Credential Manager application stores this information in the Windows account of the currently logged on user, instead of the LocalSystem account.

### Download the AWS IoT Greengrass Core software
<a name="download-greengrass-core-v2-fleet"></a>

You can download the latest version of the AWS IoT Greengrass Core software from the following location:
+ [https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip](https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip)

**Note**
You can download a specific version of the AWS IoT Greengrass Core software from the following location. Replace {{version}} with the version to download.

```
https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-{{version}}.zip
```

**To download the AWS IoT Greengrass Core software**

1. <a name="installation-download-ggc-software-step"></a>On your core device, download the AWS IoT Greengrass Core software to a file named `greengrass-nucleus-latest.zip`.

------
#### [ Linux or Unix ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip -OutFile greengrass-nucleus-latest.zip
   ```

------

   <a name="core-software-license"></a>By downloading this software, you agree to the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

1. <a name="verify-gg-nucleus-signature"></a>(Optional) To verify the Greengrass nucleus software signature
**Note**
This feature is available with Greengrass nucleus version 2.9.5 and later.

   1. Use the following command to verify your Greengrass nucleus artifact's signature:

------
#### [ Linux or Unix ]

      ```
      jarsigner -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------
#### [ Windows Command Prompt (CMD) ]

      The file name might look different depending on the JDK version you install. Replace {{`jdk17.0.6_10`}} with the JDK version you installed.

      ```
      "C:\\Program Files\\Amazon Corretto\\{{jdk17.0.6_10}}\\bin\\jarsigner.exe" -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------
#### [ PowerShell ]

      The file name might look different depending on the JDK version you install. Replace {{`jdk17.0.6_10`}} with the JDK version you installed.

      ```
      'C:\\Program Files\\Amazon Corretto\\{{jdk17.0.6_10}}\\bin\\jarsigner.exe' -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------

   1. The `jarsigner` invocation yields output that indicates the results of the verification.

      1. If the Greengrass nucleus zip file is signed, the output contains the following statement:

         ```
         jar verified.
         ```

      1. If the Greengrass nucleus zip file isn't signed, the output contains the following statement:

         ```
         jar is unsigned.
         ```

   1. If you provided the Jarsigner `-certs` option along with `-verify` and `-verbose` options, the output also includes detailed signer certificate information.

1. <a name="installation-unzip-ggc-software-step"></a>Unzip the AWS IoT Greengrass Core software to a folder on your device. Replace {{GreengrassInstaller}} with the folder that you want to use.

------
#### [ Linux or Unix ]

   ```
   unzip greengrass-nucleus-latest.zip -d {{GreengrassInstaller}} && rm greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   mkdir {{GreengrassInstaller}} && tar -xf greengrass-nucleus-latest.zip -C {{GreengrassInstaller}} && del greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   Expand-Archive -Path greengrass-nucleus-latest.zip -DestinationPath .\\{{GreengrassInstaller}}
   rm greengrass-nucleus-latest.zip
   ```

------

1. (Optional) Run the following command to see the version of the AWS IoT Greengrass Core software.

   ```
   java -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar --version
   ```

**Important**  <a name="installer-folder-2.4.0-warning"></a>
If you install a version of the Greengrass nucleus earlier than v2.4.0, don't remove this folder after you install the AWS IoT Greengrass Core software. The AWS IoT Greengrass Core software uses the files in this folder to run.
If you downloaded the latest version of the software, you install v2.4.0 or later, and you can remove this folder after you install the AWS IoT Greengrass Core software.

### Download the AWS IoT fleet provisioning plugin
<a name="download-fleet-provisioning-plugin"></a>

You can download the latest version of the AWS IoT fleet provisioning plugin from the following location:
+ [https://d2s8p88vqu9w66.cloudfront.net/releases/aws-greengrass-FleetProvisioningByClaim/fleetprovisioningbyclaim-latest.jar](https://d2s8p88vqu9w66.cloudfront.net/releases/aws-greengrass-FleetProvisioningByClaim/fleetprovisioningbyclaim-latest.jar)

**Note**
You can download a specific version of the AWS IoT fleet provisioning plugin from the following location. Replace {{version}} with the version to download. For more information about each version of the fleet provisioning plugin, see [AWS IoT fleet provisioning plugin changelog](fleet-provisioning-changelog.md).

```
https://d2s8p88vqu9w66.cloudfront.net/releases/aws-greengrass-FleetProvisioningByClaim/fleetprovisioningbyclaim-{{version}}.jar
```

The fleet provisioning plugin is open source. To view its source code, see the [AWS IoT fleet provisioning plugin](https://github.com/aws-greengrass/aws-greengrass-fleet-provisioning-by-claim) on GitHub.

**To download the AWS IoT fleet provisioning plugin**
+ On your device, download the AWS IoT fleet provisioning plugin to a file named `aws.greengrass.FleetProvisioningByClaim.jar`. Replace {{GreengrassInstaller}} with the folder that you want to use.

------
#### [ Linux or Unix ]

  ```
  curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/aws-greengrass-FleetProvisioningByClaim/fleetprovisioningbyclaim-latest.jar > {{GreengrassInstaller}}/aws.greengrass.FleetProvisioningByClaim.jar
  ```

------
#### [ Windows Command Prompt (CMD) ]

  ```
  curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/aws-greengrass-FleetProvisioningByClaim/fleetprovisioningbyclaim-latest.jar > {{GreengrassInstaller}}/aws.greengrass.FleetProvisioningByClaim.jar
  ```

------
#### [ PowerShell ]

  ```
  iwr -Uri https://d2s8p88vqu9w66.cloudfront.net/releases/aws-greengrass-FleetProvisioningByClaim/fleetprovisioningbyclaim-latest.jar -OutFile {{GreengrassInstaller}}/aws.greengrass.FleetProvisioningByClaim.jar
  ```

------

  <a name="core-software-license"></a>By downloading this software, you agree to the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

### Install the AWS IoT Greengrass Core software
<a name="run-greengrass-core-v2-installer-fleet-provisioning"></a>

Run the installer with arguments that specify the following actions:
+ Install from a partial configuration file that specifies to use the fleet provisioning plugin to provision AWS resources. The AWS IoT Greengrass Core software uses a configuration file that specifies the configuration of every Greengrass component on the device. The installer creates a complete configuration file from the partial configuration file that you provide and the AWS resources that the fleet provisioning plugin creates.
+ <a name="install-argument-component-default-user"></a>Specify to use the `ggc_user` system user to run software components on the core device. On Linux devices, this command also specifies to use the `ggc_group` system group, and the installer creates the system user and group for you.
+ <a name="install-argument-system-service"></a>Set up the AWS IoT Greengrass Core software as a system service that runs at boot. On Linux devices, this requires the [Systemd](https://en.wikipedia.org/wiki/Systemd) init system.
**Important**  <a name="windows-system-service-requirement-important-note"></a>
On Windows core devices, you must set up the AWS IoT Greengrass Core software as a system service.

For more information about the arguments that you can specify, see [Installer arguments](configure-installer.md).

**Note**
<a name="jvm-tuning-note"></a>If you are running AWS IoT Greengrass on a device with limited memory, you can control the amount of memory that AWS IoT Greengrass Core software uses. To control memory allocation, you can set JVM heap size options in the `jvmOptions` configuration parameter in your nucleus component. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).

**To install the AWS IoT Greengrass Core software**

1. <a name="installer-check-greengrass-core-software-version"></a>Check the version of the AWS IoT Greengrass Core software.
   + Replace {{GreengrassInstaller}} with the path to the folder that contains the software.

   ```
   java -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar --version
   ```

1. Use a text editor to create a configuration file named `config.yaml` to provide to the installer.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano {{GreengrassInstaller}}/config.yaml
   ```

   Copy the following YAML content into the file. This partial configuration file specifies parameters for the fleet provisioning plugin. For more information about the options that you can specify, see [Configure the AWS IoT fleet provisioning plugin](fleet-provisioning-configuration.md).

------
#### [ Linux or Unix ]

   ```
   ---
   services:
     aws.greengrass.Nucleus:
       version: "{{2.18.0}}"
       configuration:
         fipsMode: "true"
         greengrassDataPlaneEndpoint: "iotData"
     aws.greengrass.FleetProvisioningByClaim:
       configuration:
         rootPath: "{{/greengrass/v2}}"
         awsRegion: "{{us-west-2}}"
         iotDataEndpoint: "{{data.iot-fips.us-west-2.amazonaws.com}}"
         iotCredEndpoint: "{{data.credentials.iot-fips.us-west-2.amazonaws.com}}"
         iotRoleAlias: "{{GreengrassCoreTokenExchangeRoleAlias}}"
         provisioningTemplate: "GreengrassFleetProvisioningTemplate"
         claimCertificatePath: "{{/greengrass/v2}}/claim-certs/claim.pem.crt"
         claimCertificatePrivateKeyPath: "{{/greengrass/v2}}/claim-certs/claim.private.pem.key"
         rootCaPath: "{{/greengrass/v2}}/AmazonRootCA1.pem"
         templateParameters:
           ThingName: "{{MyGreengrassCore}}"
           ThingGroupName: "{{MyGreengrassCoreGroup}}"
   ```

------
#### [ Windows ]

   ```
   ---
   services:
     aws.greengrass.Nucleus:
       version: "{{2.18.0}}"
     aws.greengrass.FleetProvisioningByClaim:
       configuration:
         rootPath: "{{C:\\greengrass\\v2}}"
         awsRegion: "{{us-west-2}}"
         iotDataEndpoint: "{{device-data-prefix}}-ats.iot.{{us-west-2}}.amazonaws.com"
         iotCredentialEndpoint: "{{device-credentials-prefix}}.credentials.iot.{{us-west-2}}.amazonaws.com"
         iotRoleAlias: "{{GreengrassCoreTokenExchangeRoleAlias}}"
         provisioningTemplate: "{{GreengrassFleetProvisioningTemplate}}"
         claimCertificatePath: "{{C:\\greengrass\\v2\\claim-certs\\claim.pem.crt}}"
         claimCertificatePrivateKeyPath: "{{C:\\greengrass\\v2\\claim-certs\\claim.private.pem.key}}"
         rootCaPath: "{{C:\\greengrass\\v2}}\\AmazonRootCA1.pem"
         templateParameters:
           ThingName: "{{MyGreengrassCore}}"
           ThingGroupName: "{{MyGreengrassCoreGroup}}"
   ```

------

   Then, do the following:
   + Replace {{2.18.0}} with the version of the AWS IoT Greengrass Core software.
   + Replace each instance of `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the Greengrass root folder.
**Note**
On Windows devices, you must specify path separators as double backslashes (`\\`), such as `C:\\greengrass\\v2`.
   + Replace {{us-west-2}} with the AWS Region where you created the provisioning template and other resources.
   + Replace the `iotDataEndpoint` with your AWS IoT data endpoint.
   + Replace the `iotCredentialEndpoint` with your AWS IoT credentials endpoint.
   + Replace {{GreengrassCoreTokenExchangeRoleAlias}} with the name of the token exchange role alias.
   + Replace {{GreengrassFleetProvisioningTemplate}} with the name of the fleet provisioning template.
   + Replace the `claimCertificatePath` with the path to the claim certificate on the device.
   + Replace the `claimCertificatePrivateKeyPath` with the path to the claim certificate private key on the device.
   + Replace the template parameters (`templateParameters`) with the values to use to provision the device. This example refers to the [example template](fleet-provisioning-setup.md#example-fleet-provisioning-template) that defines `ThingName` and `ThingGroupName` parameters.

1. Run the installer. Specify `--trusted-plugin` to provide the fleet provisioning plugin, and specify `--init-config` to provide the configuration file.
   + Replace `{{/greengrass/v2}}` with the Greengrass root folder.
   + Replace each instance of {{GreengrassInstaller}} with the folder where you unpacked the installer.

------
#### [ Linux or Unix ]

   ```
   sudo -E java -Droot="{{/greengrass/v2}}" -Dlog.store=FILE \
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar \
     --trusted-plugin ./{{GreengrassInstaller}}/aws.greengrass.FleetProvisioningByClaim.jar \
     --init-config ./{{GreengrassInstaller}}/config.yaml \
     --component-default-user ggc_user:ggc_group \
     --setup-system-service true
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" ^
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar ^
     --trusted-plugin ./{{GreengrassInstaller}}/aws.greengrass.FleetProvisioningByClaim.jar ^
     --init-config ./{{GreengrassInstaller}}/config.yaml ^
     --component-default-user ggc_user ^
     --setup-system-service true
   ```

------
#### [ PowerShell ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" `
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar `
     --trusted-plugin ./{{GreengrassInstaller}}/aws.greengrass.FleetProvisioningByClaim.jar `
     --init-config ./{{GreengrassInstaller}}/config.yaml `
     --component-default-user ggc_user `
     --setup-system-service true
   ```

------
**Important**  <a name="windows-system-service-installer-argument-important-note"></a>
On Windows core devices, you must specify `--setup-system-service true` to set up the AWS IoT Greengrass Core software as a system service.

   <a name="installer-setup-system-service-output-message"></a>If you specify `--setup-system-service true`, the installer prints `Successfully set up Nucleus as a system service` if it set up and ran the software as a system service. Otherwise, the installer doesn't output any message if it installs the software successfully.
**Note**  <a name="installer-deploy-dev-tools-without-provision"></a>
You can't use the `deploy-dev-tools` argument to deploy local development tools when you run the installer without the `--provision true` argument. For information about deploying the Greengrass CLI directly on your device, see [Greengrass Command Line Interface](gg-cli.md).

1. <a name="installer-verify-installation"></a>Verify the installation by viewing the files in the root folder.

------
#### [ Linux or Unix ]

   ```
   ls {{/greengrass/v2}}
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   dir {{C:\greengrass\v2}}
   ```

------
#### [ PowerShell ]

   ```
   ls {{C:\greengrass\v2}}
   ```

------

   If the installation succeeded, the root folder contains several folders, such as `config`, `packages`, and `logs`.

<a name="install-greengrass-core-run-software"></a>If you installed the AWS IoT Greengrass Core software as a system service, the installer runs the software for you. Otherwise, you must run the software manually. For more information, see [Run the AWS IoT Greengrass Core software](run-greengrass-core-v2.md).

<a name="install-greengrass-core-next-steps-intro"></a>For more information about how to configure and use the software and AWS IoT Greengrass, see the following:<a name="install-greengrass-core-next-steps-links"></a>
+ [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md)
+ [Develop AWS IoT Greengrass components](develop-greengrass-components.md)
+ [Deploy AWS IoT Greengrass components to devices](manage-deployments.md)
+ [Greengrass Command Line Interface](gg-cli.md)

## Install FIPS endpoints with auto resource provisioning
<a name="FIPS-auto-installation"></a>

The AWS IoT Greengrass Core software includes an installer that sets up your device as a Greengrass core device. To set up a device quickly, the installer can provision the AWS IoT thing, AWS IoT thing group, IAM role, and AWS IoT role alias that the core device requires to operate. The installer can also deploy the local development tools to the core device, so you can use the device to develop and test custom software components. The installer requires AWS credentials to provision these resources and create the deployment.

If you can't provide AWS credentials to the device, you can provision the AWS resources that the core device requires to operate. You can also deploy the development tools to a core device to use as a development device. This enables you to provide fewer permissions to the device when you run the installer. For more information, see [Install AWS IoT Greengrass Core software with manual resource provisioning](manual-installation.md).

**Important**  <a name="install-greengrass-core-requirements-note"></a>
Before you download the AWS IoT Greengrass Core software, check that your core device meets the [requirements](greengrass-nucleus-component.md#greengrass-v2-requirements) to install and run the AWS IoT Greengrass Core software v2.0.

**Topics**
+ [Set up the device environment](#set-up-device-environment)
+ [Provide AWS credentials to the device](#provide-installer-aws-credentials-auto)
+ [Download the AWS IoT Greengrass Core software](#download-greengrass-core-v2-auto)
+ [Install the AWS IoT Greengrass Core software](#run-greengrass-core-v2-installer-auto)

### Set up the device environment
<a name="set-up-device-environment"></a>

Follow the steps in this section to set up a Linux or Windows device to use as your AWS IoT Greengrass core device.

#### Set up a Linux device
<a name="set-up-linux-device-environment"></a><a name="set-up-linux-device-environment-procedure"></a>

**To set up a Linux device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required. The following commands show you how to install OpenJDK on your device.
   + For Debian-based or Ubuntu-based distributions:

     ```
     sudo apt install default-jdk
     ```
   + For Red Hat-based distributions:

     ```
     sudo yum install java-11-openjdk-devel
     ```
   + For Amazon Linux 2:

     ```
     sudo amazon-linux-extras install java-openjdk11
     ```
   + For Amazon Linux 2023:

     ```
     sudo dnf install java-11-amazon-corretto -y
     ```

   When the installation completes, run the following command to verify that Java runs on your Linux device.

   ```
   java -version
   ```

   The command prints the version of Java that runs on the device. For example, on a Debian-based distribution, the output might look similar to the following sample.

   ```
   openjdk version "11.0.9.1" 2020-11-04
   OpenJDK Runtime Environment (build 11.0.9.1+1-post-Debian-1deb10u2)
   OpenJDK 64-Bit Server VM (build 11.0.9.1+1-post-Debian-1deb10u2, mixed mode)
   ```

1. (Optional) Create the default system user and group that runs components on the device. You can also choose to let the AWS IoT Greengrass Core software installer create this user and group during installation with the `--component-default-user` installer argument. For more information, see [Installer arguments](configure-installer.md).

   ```
   sudo useradd --system --create-home ggc_user
   sudo groupadd --system ggc_group
   ```

1. Verify that the user that runs the AWS IoT Greengrass Core software (typically `root`), has permission to run `sudo` with any user and any group.

   1. Run the following command to open the `/etc/sudoers` file.

      ```
      sudo visudo
      ```

   1. Verify that the permission for the user looks like the following example.

      ```
      root    ALL=(ALL:ALL) ALL
      ```

1. (Optional) To [run containerized Lambda functions](run-lambda-functions.md), you must enable [cgroups](https://en.wikipedia.org/wiki/Cgroups) v1, and you must enable and mount the *memory* and *devices* cgroups. If you don't plan to run containerized Lambda functions, you can skip this step.

   To enable these cgroups options, boot the device with the following Linux kernel parameters.

   ```
   cgroup_enable=memory cgroup_memory=1 systemd.unified_cgroup_hierarchy=0
   ```

   For information about viewing and setting kernel parameters for your device, see the documentation for your operating system and boot loader. Follow the instructions to permanently set the kernel parameters.

1. Install all other required dependencies on your device as indicated by the list of requirements in [Device requirements](greengrass-nucleus-component.md#greengrass-v2-requirements).

#### Set up a Windows device
<a name="set-up-windows-device-environment"></a>

**Note**
This feature is available for v2.5.0 and later of the [Greengrass nucleus component](greengrass-nucleus-component.md).<a name="set-up-windows-device-environment-procedure"></a>

**To set up a Windows device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required.

1. Check whether Java is available on the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) system variable, and add it if not. The LocalSystem account runs the AWS IoT Greengrass Core software, so you must add Java to the PATH system variable instead of the PATH user variable for your user. Do the following:

   1. Press the Windows key to open the start menu.

   1. Type **environment variables** to search for the system options from the start menu.

   1. In the start menu search results, choose **Edit the system environment variables** to open the **System properties** window.

   1. Choose **Environment variables...** to open the **Environment Variables** window.

   1. Under **System variables**, select **Path**, and then choose **Edit**. In the **Edit environment variable** window, you can view each path on a separate line.

   1. Check if the path to the Java installation's `bin` folder is present. The path might look similar to the following example.

      ```
      C:\\Program Files\\Amazon Corretto\\jdk11.0.13_8\\bin
      ```

   1. If the Java installation's `bin` folder is missing from **Path**, choose **New** to add it, and then choose **OK**.

1. <a name="set-up-windows-device-environment-open-cmd"></a>Open the Windows Command Prompt (`cmd.exe`) as an administrator.

1. <a name="set-up-windows-device-environment-create"></a>Create the default user in the LocalSystem account on the Windows device. Replace {{password}} with a secure password.

   ```
   net user /add ggc_user {{password}}
   ```
**Tip**  <a name="windows-password-expiration-tip"></a>
Depending on your Windows configuration, the user's password might be set to expire at a date in the future. To ensure your Greengrass applications continue to operate, track when the password expires, and update it before it expires. You can also set the user's password to never expire.
To check when a user and its password expire, run the following command.

     ```
     net user {{ggc_user}} | findstr /C:expires
     ```
To set a user's password to never expire, run the following command.

     ```
     wmic UserAccount where "Name='{{ggc_user}}'" set PasswordExpires=False
     ```
If you’re using Windows 10 or later where the [`wmic` command is deprecated](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic), run the following PowerShell command.

     ```
     Get-CimInstance -Query "SELECT * from Win32_UserAccount WHERE name = '{{ggc_user}}'" | Set-CimInstance -Property @{PasswordExpires="False"}
     ```

1. <a name="set-up-windows-device-psexec"></a>Download and install the [PsExec utility](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) from Microsoft on the device.

1. <a name="set-up-windows-device-credentials"></a>Use the PsExec utility to store the user name and password for the default user in the Credential Manager instance for the LocalSystem account. Replace {{password}} with the user's password that you set earlier.

   ```
   psexec -s cmd /c cmdkey /generic:ggc_user /user:ggc_user /pass:{{password}}
   ```

   If the **PsExec License Agreement** opens, choose **Accept** to agree to the license and run the command.
**Note**
On Windows devices, the LocalSystem account runs the Greengrass nucleus, and you must use the PsExec utility to store the default user information in the LocalSystem account. Using the Credential Manager application stores this information in the Windows account of the currently logged on user, instead of the LocalSystem account.

### Provide AWS credentials to the device
<a name="provide-installer-aws-credentials-auto"></a>

Provide your AWS credentials to your device so that the installer can provision the required AWS resources. For more information about the required permissions, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md).

**To provide AWS credentials to the device**
+ <a name="installer-export-aws-credentials"></a>Provide your AWS credentials to the device so that the installer can provision the AWS IoT and IAM resources for your core device. To increase security, we recommend that you get temporary credentials for an IAM role that allows only the minimum permissions necessary to provision. For more information, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md).
**Note**
The installer doesn't save or store your credentials.

  On your device, do one of the following to retrieve credentials and make them available to the AWS IoT Greengrass Core software installer:
  + (Recommended) Use temporary credentials from AWS IAM Identity Center

    1. Provide the access key ID, secret access key, and session token from the IAM Identity Center. For more information, see **Manual credential refresh** in [ Getting and refreshing temporary credentials](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html#how-to-get-temp-credentials) in the *IAM Identity Center user guide*.

    1. Run the following commands to provide the credentials to the AWS IoT Greengrass Core software.

------
#### [ Linux or Unix ]

       ```
       export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
       export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
       export AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
       ```

------
#### [ Windows Command Prompt (CMD) ]

       ```
       set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
       set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
       set AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
       ```

------
#### [ PowerShell ]

       ```
       $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
       $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
       $env:AWS_SESSION_TOKEN="{{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}"
       ```

------
  + Use temporary security credentials from an IAM role:

    1. Provide the access key ID, secret access key, and session token from an IAM role that you assume. For more information about how to retrieve these credentials, see [Requesting temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*.

    1. Run the following commands to provide the credentials to the AWS IoT Greengrass Core software.

------
#### [ Linux or Unix ]

       ```
       export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
       export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
       export AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
       ```

------
#### [ Windows Command Prompt (CMD) ]

       ```
       set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
       set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
       set AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
       ```

------
#### [ PowerShell ]

       ```
       $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
       $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
       $env:AWS_SESSION_TOKEN="{{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}"
       ```

------
  + Use long-term credentials from an IAM user:

    1. Provide the access key ID and secret access key for your IAM user. You can create an IAM user for provisioning that you later delete. For the IAM policy to give the user, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md). For more information about how to retrieve long-term credentials, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.

    1. Run the following commands to provide the credentials to the AWS IoT Greengrass Core software.

------
#### [ Linux or Unix ]

       ```
       export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
       export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
       ```

------
#### [ Windows Command Prompt (CMD) ]

       ```
       set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
       set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
       ```

------
#### [ PowerShell ]

       ```
       $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
       $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
       ```

------

    1. (Optional) If you created an IAM user to provision your Greengrass device, delete the user.

    1. (Optional) If you used the access key ID and secret access key from an existing IAM user, update the keys for the user so that they are no longer valid. For more information, see [ Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *AWS Identity and Access Management user guide*.

### Download the AWS IoT Greengrass Core software
<a name="download-greengrass-core-v2-auto"></a>

You can download the latest version of the AWS IoT Greengrass Core software from the following location:
+ [https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip](https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip)

**Note**
You can download a specific version of the AWS IoT Greengrass Core software from the following location. Replace {{version}} with the version to download.

```
https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-{{version}}.zip
```

**To download the AWS IoT Greengrass Core software**

1. <a name="installation-download-ggc-software-step"></a>On your core device, download the AWS IoT Greengrass Core software to a file named `greengrass-nucleus-latest.zip`.

------
#### [ Linux or Unix ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip -OutFile greengrass-nucleus-latest.zip
   ```

------

   <a name="core-software-license"></a>By downloading this software, you agree to the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

1. <a name="verify-gg-nucleus-signature"></a>(Optional) To verify the Greengrass nucleus software signature
**Note**
This feature is available with Greengrass nucleus version 2.9.5 and later.

   1. Use the following command to verify your Greengrass nucleus artifact's signature:

------
#### [ Linux or Unix ]

      ```
      jarsigner -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------
#### [ Windows Command Prompt (CMD) ]

      The file name might look different depending on the JDK version you install. Replace {{`jdk17.0.6_10`}} with the JDK version you installed.

      ```
      "C:\\Program Files\\Amazon Corretto\\{{jdk17.0.6_10}}\\bin\\jarsigner.exe" -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------
#### [ PowerShell ]

      The file name might look different depending on the JDK version you install. Replace {{`jdk17.0.6_10`}} with the JDK version you installed.

      ```
      'C:\\Program Files\\Amazon Corretto\\{{jdk17.0.6_10}}\\bin\\jarsigner.exe' -verify -certs -verbose greengrass-nucleus-latest.zip
      ```

------

   1. The `jarsigner` invocation yields output that indicates the results of the verification.

      1. If the Greengrass nucleus zip file is signed, the output contains the following statement:

         ```
         jar verified.
         ```

      1. If the Greengrass nucleus zip file isn't signed, the output contains the following statement:

         ```
         jar is unsigned.
         ```

   1. If you provided the Jarsigner `-certs` option along with `-verify` and `-verbose` options, the output also includes detailed signer certificate information.

1. <a name="installation-unzip-ggc-software-step"></a>Unzip the AWS IoT Greengrass Core software to a folder on your device. Replace {{GreengrassInstaller}} with the folder that you want to use.

------
#### [ Linux or Unix ]

   ```
   unzip greengrass-nucleus-latest.zip -d {{GreengrassInstaller}} && rm greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   mkdir {{GreengrassInstaller}} && tar -xf greengrass-nucleus-latest.zip -C {{GreengrassInstaller}} && del greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   Expand-Archive -Path greengrass-nucleus-latest.zip -DestinationPath .\\{{GreengrassInstaller}}
   rm greengrass-nucleus-latest.zip
   ```

------

1. (Optional) Run the following command to see the version of the AWS IoT Greengrass Core software.

   ```
   java -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar --version
   ```

**Important**  <a name="installer-folder-2.4.0-warning"></a>
If you install a version of the Greengrass nucleus earlier than v2.4.0, don't remove this folder after you install the AWS IoT Greengrass Core software. The AWS IoT Greengrass Core software uses the files in this folder to run.
If you downloaded the latest version of the software, you install v2.4.0 or later, and you can remove this folder after you install the AWS IoT Greengrass Core software.

### Install the AWS IoT Greengrass Core software
<a name="run-greengrass-core-v2-installer-auto"></a>

Run the installer with arguments that specify to do the following:
+ <a name="install-argument-aws-resources"></a>Create the AWS resources that the core device requires to operate.
+ <a name="install-argument-component-default-user"></a>Specify to use the `ggc_user` system user to run software components on the core device. On Linux devices, this command also specifies to use the `ggc_group` system group, and the installer creates the system user and group for you.
+ <a name="install-argument-system-service"></a>Set up the AWS IoT Greengrass Core software as a system service that runs at boot. On Linux devices, this requires the [Systemd](https://en.wikipedia.org/wiki/Systemd) init system.
**Important**  <a name="windows-system-service-requirement-important-note"></a>
On Windows core devices, you must set up the AWS IoT Greengrass Core software as a system service.

To set up a development device with local development tools, specify the `--deploy-dev-tools true` argument. The local development tools can take up to a minute to deploy after the installation completes.

For more information about the arguments that you can specify, see [Installer arguments](configure-installer.md).

**Note**
<a name="jvm-tuning-note"></a>If you are running AWS IoT Greengrass on a device with limited memory, you can control the amount of memory that AWS IoT Greengrass Core software uses. To control memory allocation, you can set JVM heap size options in the `jvmOptions` configuration parameter in your nucleus component. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).

**To install the AWS IoT Greengrass Core software**

1. Use a text editor to create a configuration file named `config.yaml` to provide to the installer.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano {{GreengrassInstaller}}/config.yaml
   ```

   Copy the following YAML content into the file. This partial configuration file specifies system parameters and Greengrass nucleus parameters.

   ```
   ---
   services:
     aws.greengrass.Nucleus:
       configuration:
         fipsMode: "true"
         iotDataEndpoint: "{{data.iot-fips.us-west-2.amazonaws.com}}"
         iotCredEndpoint: "{{data.credentials.iot-fips.us-west-2.amazonaws.com}}"
         greengrassDataPlaneEndpoint: "iotData"
   ```
   + Replace {{us-west-2}} with the AWS Region where you created the resources.
   + Replace the {{iotDataEndpoint}} with your AWS IoT data endpoint.
   + Replace the {{iotCredEndpoint}} with your AWS IoT credentials endpoint.

1. Run the AWS IoT Greengrass Core installer. Replace argument values in your command as follows.
**Note**
Windows has a path length limitation of 260 characters. If you are using Windows, use a root folder like `C:\greengrass\v2` or `D:\greengrass\v2` to keep the Greengrass components paths under the 260 character limit.<a name="installer-replace-arguments"></a>

   1. `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}}: The path to the root folder to use to install the AWS IoT Greengrass Core software.

   1. {{GreengrassInstaller}}. The path to the folder where you unpacked the AWS IoT Greengrass Core software installer.

   1. {{region}}. The AWS Region in which to find or create resources.

   1. {{MyGreengrassCore}}. The name of the AWS IoT thing for your Greengrass core device. If the thing doesn't exist, the installer creates it. The installer downloads the certificates to authenticate as the AWS IoT thing. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).
**Note**  <a name="install-argument-thing-name-constraint"></a>
The thing name can't contain colon (`:`) characters.

   1. {{MyGreengrassCoreGroup}}. The name of AWS IoT thing group for your Greengrass core device. If the thing group doesn't exist, the installer creates it and adds the thing to it. If the thing group exists and has an active deployment, the core device downloads and runs the software that the deployment specifies.
**Note**  <a name="install-argument-thing-group-name-constraint"></a>
The thing group name can't contain colon (`:`) characters.

   1. {{GreengrassV2IoTThingPolicy}}. The name of the AWS IoT policy that allows the Greengrass core devices to communicate with AWS IoT and AWS IoT Greengrass. If the AWS IoT policy doesn't exist, the installer creates a permissive AWS IoT policy with this name. You can restrict this policy's permissions for you use case. For more information, see [Minimal AWS IoT policy for AWS IoT Greengrass V2 core devices](device-auth.md#greengrass-core-minimal-iot-policy).

   1. {{GreengrassV2TokenExchangeRole}}. The name of the IAM role that allows the Greengrass core device to get temporary AWS credentials. If the role doesn't exist, the installer creates it and creates and attaches a policy named `{{GreengrassV2TokenExchangeRole}}Access`. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).

   1. {{GreengrassCoreTokenExchangeRoleAlias}}. The alias to the IAM role that allows the Greengrass core device to get temporary credentials later. If the role alias doesn't exist, the installer creates it and points it to the IAM role that you specify. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).

------
#### [ Linux or Unix ]

   ```
   sudo -E java -Droot="{{/greengrass/v2}}" -Dlog.store=FILE \
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar \
     --aws-region {{region}} \
     --thing-name {{MyGreengrassCore}} \
     --thing-group-name {{MyGreengrassCoreGroup}} \
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} \
     --tes-role-name {{GreengrassV2TokenExchangeRole}} \
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} \
     --component-default-user ggc_user:ggc_group \
     --provision true \
     --init-config ./GreengrassInstaller/config.yaml \
     --setup-system-service true
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" ^
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar ^
     --aws-region {{region}} ^
     --thing-name {{MyGreengrassCore}} ^
     --thing-group-name {{MyGreengrassCoreGroup}} ^
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} ^
     --tes-role-name {{GreengrassV2TokenExchangeRole}} ^
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} ^
     --component-default-user ggc_user ^
     --provision true ^
     --setup-system-service true
   ```

------
#### [ PowerShell ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" `
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar `
     --aws-region {{region}} `
     --thing-name {{MyGreengrassCore}} `
     --thing-group-name {{MyGreengrassCoreGroup}} `
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} `
     --tes-role-name {{GreengrassV2TokenExchangeRole}} `
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} `
     --component-default-user ggc_user `
     --provision true `
     --setup-system-service true
   ```

------
**Important**  <a name="windows-system-service-installer-argument-important-note"></a>
On Windows core devices, you must specify `--setup-system-service true` to set up the AWS IoT Greengrass Core software as a system service.

   The installer prints the following messages if it succeeds:
   + If you specify `--provision`, the installer prints `Successfully configured Nucleus with provisioned resource details` if it configured the resources successfully.
   + If you specify `--deploy-dev-tools`, the installer prints `Configured Nucleus to deploy aws.greengrass.Cli component` if it created the deployment successfully.
   + If you specify `--setup-system-service true`, the installer prints `Successfully set up Nucleus as a system service` if it set up and ran the software as a service.
   + If you don't specify `--setup-system-service true`, the installer prints `Launched Nucleus successfully` if it succeeded and ran the software.

1. Skip this step if you installed [Greengrass nucleus](greengrass-nucleus-component.md) v2.0.4 or later. If you downloaded the latest version of the software, you installed v2.0.4 or later.

   Run the following command to set the required file permissions for your AWS IoT Greengrass Core software root folder. Replace `{{/greengrass/v2}}` with the root folder that you specified in your installation command, and replace {{/greengrass}} with the parent folder for your root folder.

   ```
   sudo chmod 755 {{/greengrass/v2}} && sudo chmod 755 {{/greengrass}}
   ```

<a name="install-greengrass-core-run-software"></a>If you installed the AWS IoT Greengrass Core software as a system service, the installer runs the software for you. Otherwise, you must run the software manually. For more information, see [Run the AWS IoT Greengrass Core software](run-greengrass-core-v2.md).

**Note**
By default, the IAM role that the installer creates doesn't allow access to component artifacts in S3 buckets. To deploy custom components that define artifacts in Amazon S3, you must add permissions to the role to allow your core device to retrieve component artifacts. For more information, see [Allow access to S3 buckets for component artifacts](device-service-role.md#device-service-role-access-s3-bucket).
If you don't yet have an S3 bucket for component artifacts, you can add these permissions later after you create a bucket.

<a name="install-greengrass-core-next-steps-intro"></a>For more information about how to configure and use the software and AWS IoT Greengrass, see the following:<a name="install-greengrass-core-next-steps-links"></a>
+ [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md)
+ [Develop AWS IoT Greengrass components](develop-greengrass-components.md)
+ [Deploy AWS IoT Greengrass components to devices](manage-deployments.md)
+ [Greengrass Command Line Interface](gg-cli.md)

## FIPS compliance first party components
<a name="FIPS-compliance"></a>

|  |  |
| --- | --- |
| aws.greengrass.Nucleus | data.iot-fips.{{us-east-1}}.amazonaws.com |
|  | greengrass-fips.{{us-east-1}}.amazonaws.com |
|  | data.credentials.iot-fips.{{us-east-1}}.amazonaws.com |
| aws.greengrass.TokenExchangeService | data.credentials.iot-fips.{{us-east-1}}.amazonaws.com |
| aws.greengrass.Cli |  |
| aws.greengrass.StreamManager | [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/FIPS.html) Stream manager does not support AWS IoT Analytics FIPS endpoint  |
| aws.greengrass.LogManager | logs-fips.{{us-east-1}}.amazonaws.com |
| aws.greengrass.crypto.Pkcs11Provider |  |
| aws.greengrass.ShadowManager |  |
| aws.greengrass.DockerApplicationManager | ecr-fips.{{us-east-1}}.amazonaws.com |
| aws.greengrass.SecretManager | secretsmanager-fips.{{us-east-1}}.amazonaws.com |
| aws.greengrass.telemetry.NucleusEmitter |  |
| aws.greengrass.clientdevices.IPDetector |  |
| aws.greengrass.DiskSpooler |  |
