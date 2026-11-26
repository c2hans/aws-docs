---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/proxy-encryption.html
---

# Encrypt a proxy configuration with a customer managed key

Elastic Load Balancing for Envoy (ELB for Envoy) always encrypts your proxy's configuration file and configuration archive at rest. You have two options for the encryption key:
+ **AWS owned key** (default) – ELB for Envoy encrypts your configuration with an AWS owned key, and you don't need to set anything up. You can't view, manage, or audit AWS owned keys.
+ **Customer managed key** – ELB for Envoy encrypts your configuration with a key in AWS Key Management Service (AWS KMS) that you create and own. Its key policy controls access, and you can audit the key's use in AWS CloudTrail.

Proxy metadata, such as the proxy's name, tags, and attributes, isn't encrypted with your customer managed key.

## How encryption with a customer managed key works
<a name="proxy-encryption-how-it-works"></a>

When you specify a customer managed key, ELB for Envoy uses envelope encryption. For each configuration version, it does the following:

1. Calls `GenerateDataKey` on your key.

1. Encrypts your configuration with the returned data key.

1. Stores the encrypted configuration with the encrypted data key.

To read the configuration, ELB for Envoy calls `Decrypt` on your key to decrypt the data key.

ELB for Envoy calls AWS KMS in two ways:
+ **With your credentials**, through forward access sessions, when you call `CreateProxy`, `UpdateProxyConfiguration`, or `GetProxyConfigurationContents`.
+ **As the service principal `elasticloadbalancing.amazonaws.com`**, to deliver configuration to the proxy's nodes.

Every call uses an encryption context that binds the data key to one proxy. The context key is `aws:elasticloadbalancing:proxy-arn`, and its value is the proxy ARN. A data key issued for one proxy can't decrypt another proxy's configuration.

ELB for Envoy doesn't create grants on your key, doesn't require a customer-provided role, and doesn't cache data keys.

## Key requirements
<a name="proxy-encryption-key-requirements"></a>

The customer managed key must meet all of the following requirements:
+ It's a symmetric encryption key (`SYMMETRIC_DEFAULT` key spec, `ENCRYPT_DECRYPT` key usage).
+ It's enabled.
+ It's in the same AWS account and Region as the proxy. Multi-Region keys aren't supported.

Specify the full key ARN. Key IDs and aliases aren't accepted.

When a request sets a key, or an update keeps the proxy's current key, ELB for Envoy calls `DescribeKey` and a `Decrypt` with `DryRun` to check the key and your key policy. If either check fails, the request fails. See [Errors](#proxy-encryption-errors).

## Key policy
<a name="proxy-encryption-key-policy"></a>

The key policy must allow two principals to use the key:
+ The role that calls the ELB for Envoy APIs. It needs `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt`.
+ The ELB for Envoy service principal, `elasticloadbalancing.amazonaws.com`, which decrypts your configuration to deliver it to the proxy's nodes.

The following example key policy grants the permissions that ELB for Envoy needs.

```json
{
  "Version": "2012-10-17",
  "Id": "elb-for-envoy-proxy-configuration-key-policy",
  "Statement": [
    {
      "Sid": "EnableKeyAdministration",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{123456789012}}:root" },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowElbForEnvoyToDescribeKey",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{123456789012}}:role/{{ProxyAdminRole}}" },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "elasticloadbalancing.{{us-east-1}}.amazonaws.com",
          "kms:CallerAccount": "{{123456789012}}"
        }
      }
    },
    {
      "Sid": "AllowElbForEnvoyToEncryptAndDecryptProxyConfiguration",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{123456789012}}:role/{{ProxyAdminRole}}" },
      "Action": ["kms:GenerateDataKey", "kms:Decrypt"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "elasticloadbalancing.{{us-east-1}}.amazonaws.com",
          "kms:CallerAccount": "{{123456789012}}"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:elasticloadbalancing:proxy-arn": "arn:aws:elasticloadbalancing:{{us-east-1}}:{{123456789012}}:proxy/*"
        }
      }
    },
    {
      "Sid": "AllowElbForEnvoyToDecryptForProxyNodes",
      "Effect": "Allow",
      "Principal": { "Service": "elasticloadbalancing.amazonaws.com" },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "{{123456789012}}" },
        "ArnLike": { "aws:SourceArn": "arn:aws:elasticloadbalancing:{{us-east-1}}:{{123456789012}}:proxy/*" },
        "StringLike": {
          "kms:EncryptionContext:aws:elasticloadbalancing:proxy-arn": "arn:aws:elasticloadbalancing:{{us-east-1}}:{{123456789012}}:proxy/*"
        }
      }
    }
  ]
}
```

Replace the following tokens:
+ {{123456789012}} with your AWS account ID.
+ {{us-east-1}} with the proxy's Region.
+ {{ProxyAdminRole}} with the role that calls the ELB for Envoy APIs.

Each statement grants the following:
+ `EnableKeyAdministration` – Gives your account full control of the key. Scope it to your key administrators as your security practices require.
+ `AllowElbForEnvoyToDescribeKey` – Validates the key when a request specifies it.
+ `AllowElbForEnvoyToEncryptAndDecryptProxyConfiguration` – Creates data keys, runs the `DryRun` check, re-encrypts during key changes, and returns configuration from `GetProxyConfigurationContents`.
+ `AllowElbForEnvoyToDecryptForProxyNodes` – Decrypts data keys to deliver configuration to the proxy's nodes.

## Scope down access to the key
<a name="proxy-encryption-scope-down"></a>

The example key policy uses the following conditions to limit access to the key:
+ `kms:ViaService` (`elasticloadbalancing.{{us-east-1}}.amazonaws.com`) limits calls made with your credentials to ELB for Envoy.
+ The encryption context key `aws:elasticloadbalancing:proxy-arn` is set to the proxy ARN on every `GenerateDataKey` and `Decrypt`. Use it to limit the key to all proxies or to specific proxies.
+ `aws:SourceArn` and `aws:SourceAccount` are set on calls that the service principal makes, which protects against the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html).

To limit the key to one proxy, replace every `proxy/*` in the key policy with the following value. Replace {{my-proxy}} with the name of your proxy.

```json
"arn:aws:elasticloadbalancing:{{us-east-1}}:{{123456789012}}:proxy/{{my-proxy}}/*"
```

These conditions apply to the key policy statements. If you also grant key access through IAM policies, add the same `kms:ViaService` and encryption context conditions to those policies.

## Create a customer managed key
<a name="proxy-encryption-create-key"></a>

Create a key using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To create a customer managed key**

1. Open the [AWS KMS console](https://console.aws.amazon.com/kms/home).

1. Choose **Create key**.

1. For **Key type**, choose **Symmetric**.

1. For **Key usage**, choose **Encrypt and decrypt**.

1. Enter an alias for the key, for example `my-proxy-key`.

1. On the key policy page, replace the policy with the key policy in [Key policy](#proxy-encryption-key-policy).

1. Finish creating the key, and note the key ARN.

------
#### [ AWS CLI ]

**To create a customer managed key**

1. Save the key policy in [Key policy](#proxy-encryption-key-policy) as `key-policy.json`.

1. Create the key.

   ```
   aws kms create-key \
       --key-spec SYMMETRIC_DEFAULT \
       --key-usage ENCRYPT_DECRYPT \
       --policy file://key-policy.json
   ```

1. Note the key ARN in the `KeyMetadata.Arn` field of the output.

------
#### [ CloudFormation ]

You can create the key with the [`AWS::KMS::Key`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-key.html) resource. Set `KeySpec` to `SYMMETRIC_DEFAULT`, `KeyUsage` to `ENCRYPT_DECRYPT`, and `KeyPolicy` to the key policy in [Key policy](#proxy-encryption-key-policy).

```yaml
Resources:
  ProxyKey:
    Type: AWS::KMS::Key
    Properties:
      KeySpec: SYMMETRIC_DEFAULT
      KeyUsage: ENCRYPT_DECRYPT
      KeyPolicy: # see the key policy referenced above
```

------

## Create a proxy with a customer managed key
<a name="proxy-encryption-create-proxy"></a>

Create a proxy with a customer managed key using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To create a proxy with a customer managed key**

1. Start creating a proxy as described in [Create a proxy](create-proxy.md).

1. On the **Configure proxy** step, expand **Advanced configurations**.

1. For **Encryption type**, choose **Server-side encryption with customer-managed key from AWS Key Management Service**.

1. For **AWS KMS key**, choose your key.

1. Complete the remaining steps and choose **Create proxy**.

------
#### [ AWS CLI ]

The following AWS CLI command creates a proxy that encrypts its configuration with your customer managed key. The `customerKmsKeyArn` field in the `--cli-input-json` object specifies the key. Specify the full key ARN.

Replace the following values in the command:
+ `{{account-id}}` – Your AWS account ID.
+ `{{proxy-role-name}}` – The name of your proxy role.
+ `{{region}}` and `{{key-id}}` – The values from your key ARN.
+ `{{subnet-id-1}}` and `{{subnet-id-2}}` – Your subnet IDs.
+ `{{security-group-id}}` – Your security group ID.
+ `/tmp/config.yaml` and `/tmp/archive.zip` – The paths to your configuration file and configuration archive.

```bash
aws elb-proxy create-proxy \
  --cli-input-json '{
    "name": "my-proxy",
    "type": "envoy",
    "proxyVersion": "1.40",
    "roleArn": "arn:aws:iam::{{account-id}}:role/{{proxy-role-name}}",
    "customerKmsKeyArn": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
    "networkConfiguration": {
      "ipConfiguration": {
        "ipAddressingConfiguration": {
          "ipv4Addressability": "internet-facing",
          "ipv6Addressability": "off"
        }
      },
      "vpcConfiguration": {
        "subnets": [
          { "subnetId": "{{subnet-id-1}}" },
          { "subnetId": "{{subnet-id-2}}" }
        ],
        "securityGroups": [
          { "securityGroupId": "{{security-group-id}}" }
        ]
      }
    }
  }' \
  --configuration configurationFile={configurationBytes@=file:///tmp/config.yaml},configurationArchive={configurationBytes@=fileb:///tmp/archive.zip}
```

For the other inputs, see [Create a proxy](create-proxy.md).

**Note**
The `configurationArchive` is optional. When you use AWS CLI version 2, add `--cli-binary-format raw-in-base64-out`.

When you specify `customerKmsKeyArn`, ELB for Envoy validates the key, generates a data key under the proxy's encryption context, and encrypts your configuration. The proxy stays in `create-in-progress` until it's running, and then becomes `active`. To use the AWS owned key, omit `customerKmsKeyArn`.

`CreateProxy` and `GetProxy` return `customerKmsKeyArn`.

------
#### [ CloudFormation ]

Set `CustomerKmsKeyArn` on your `AWS::ElasticLoadBalancingProxy::Proxy` resource. Specify the full key ARN. Add `CustomerKmsKeyArn` to the proxy resource in [Create a proxy](create-proxy.md).

```yaml
Properties:
  CustomerKmsKeyArn: arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}
```

------

## Verify the key that a proxy uses
<a name="proxy-encryption-verify"></a>

Verify the key that a proxy uses with the console or the AWS CLI. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To view the key that a proxy uses**

1. Open the Amazon EC2 console, and in the navigation pane choose **Proxies**.

1. Choose the name of the proxy.

1. On the proxy details page, check **Encryption type**. A proxy that uses your key shows **Server-side encryption with customer-managed key** and the key ARN.

------
#### [ AWS CLI ]

Run **get-proxy**. When the proxy uses a customer managed key, the output includes `customerKmsKeyArn`.

```
aws elb-proxy get-proxy --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy.

**get-proxy-configuration-contents** also returns `customerKmsKeyArn`, which is the key the configuration is encrypted under.

```
aws elb-proxy get-proxy-configuration-contents \
    --proxy-identifier <proxy-arn> \
    --include-config-file
```

For a proxy that uses the AWS owned key, `customerKmsKeyArn` is absent.

------

Viewing a key is a read operation, so this task has no CloudFormation method.

## Change or remove the key
<a name="proxy-encryption-change-key"></a>

You can set a key on an existing proxy, rotate to a different key, or switch to the AWS owned key. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To change or remove the key**

1. In the Amazon EC2 console, choose **Proxies**, and choose the name of the proxy.

1. Choose **Edit configuration**.

1. Under **Encryption type**, do one of the following:
   + To set or rotate the key, choose **Server-side encryption with customer-managed key from AWS Key Management Service**, and then choose the key in **AWS KMS key**.
   + To switch to the AWS owned key, choose **Server-side encryption with Amazon-managed key**.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

`UpdateProxyConfiguration` controls the key through the `customerKmsKeyArn` and `resetCustomerKmsKeyArn` parameters.

| To | Use |
| --- | --- |
| Keep the current key | Omit both --customer-kms-key-arn and --reset-customer-kms-key-arn |
| Set or rotate to a customer managed key | --customer-kms-key-arn with the new key ARN |
| Remove the key and use the AWS owned key | --reset-customer-kms-key-arn |

If you don't specify a key, the proxy keeps its current key. If the request has no new configuration, ELB for Envoy re-encrypts the current configuration. It decrypts the current configuration with the current key, so keep that key usable until the update completes.

To set or rotate the key, specify the key ARN with **update-proxy-configuration**.

```
aws elb-proxy update-proxy-configuration \
    --proxy-identifier <proxy-arn> \
    --customer-kms-key-arn <key-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy, and {{key-arn}} with the full ARN of your key.

To remove the customer managed key and use the AWS owned key, include `--reset-customer-kms-key-arn`.

```
aws elb-proxy update-proxy-configuration \
    --proxy-identifier <proxy-arn> \
    --reset-customer-kms-key-arn
```

Replace {{proxy-arn}} with the ARN of your proxy.

------
#### [ CloudFormation ]

To set or rotate the key, change `CustomerKmsKeyArn` on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. To switch to the AWS owned key, remove the `CustomerKmsKeyArn` property and update the stack.

------

ELB for Envoy doesn't re-encrypt previous configuration versions. Each version stays encrypted under the key that was in use when you created it. ELB for Envoy deletes previous versions after about 4 days. If the most recent previous version uses the same key as the current version, ELB for Envoy keeps it so that it can roll back to it.

You can't read previous versions through the ELB for Envoy APIs. If you disable or delete a previous key, you can't decrypt the versions encrypted under it.

## When ELB for Envoy can't use your key
<a name="proxy-encryption-key-inaccessible"></a>

If you disable or delete the key, or remove the permissions that ELB for Envoy needs, the following happens:
+ The proxy's status becomes `action-required`, with the reason `CustomerKmsKeyInaccessible`. The message names the key and the AWS KMS error.
+ Running nodes keep serving their current configuration, but new configuration versions and new nodes can't get configuration.
+ If the key is disabled or deleted, `GetProxyConfigurationContents` and updates fail with `ValidationException`. If your principal's permissions are removed, they fail with `AccessDeniedException`. If only the service principal's permissions are removed, these calls still succeed, but the nodes can't decrypt the new configuration.

When you restore access, the reason clears and the proxy returns to its previous status. If you delete the key, configuration encrypted with it can't be recovered. Update the proxy with new configuration and another key, or with no key.

## Errors
<a name="proxy-encryption-errors"></a>

The following table lists common encryption errors, their causes, and how to fix them.

| Error | Cause | Fix |
| --- | --- | --- |
| ValidationException: key not usable | The key doesn't exist, is disabled, or is pending deletion. | Check the key ARN and Region, and make sure the key is enabled. |
| ValidationException: key not symmetric | The key is asymmetric. | Use a SYMMETRIC\_DEFAULT key. |
| ValidationException: wrong key usage | The key usage isn't encrypt and decrypt. | Create the key with ENCRYPT\_DECRYPT usage. |
| ValidationException: multi-Region key | The key is a multi-Region key. | Use a single-Region key. |
| AccessDeniedException on GenerateDataKey or Decrypt | The key policy doesn't grant the caller or the service principal. | Apply the key policy in [Key policy](#proxy-encryption-key-policy). |
| The proxy's status is action-required with the reason CustomerKmsKeyInaccessible | The key is disabled or deleted, or the key policy no longer grants your role or the service principal. | Restore the key or the AllowElbForEnvoyToDecryptForProxyNodes statement. See [When ELB for Envoy can't use your key](#proxy-encryption-key-inaccessible). |

## Monitor key use with AWS CloudTrail
<a name="proxy-encryption-cloudtrail"></a>

You can audit how ELB for Envoy uses your key in AWS CloudTrail. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html).

| eventName | When | Caller |
| --- | --- | --- |
| DescribeKey and Decrypt (dryRun) | CreateProxy or UpdateProxyConfiguration that sets a key, or an update that keeps the proxy's current key | Your principal |
| GenerateDataKey | CreateProxy, UpdateProxyConfiguration | Your principal |
| Decrypt | GetProxyConfigurationContents, once per component returned; UpdateProxyConfiguration, once per component carried over from the current configuration | Your principal |
| Decrypt | Each time a node fetches its configuration | elasticloadbalancing.amazonaws.com, with sourceArn and sourceAccount |

Each event's `encryptionContext` is set to the proxy ARN:

```json
{"aws:elasticloadbalancing:proxy-arn": "arn:aws:elasticloadbalancing:{{us-east-1}}:{{123456789012}}:proxy/my-proxy/0123456789abcdef"}
```
