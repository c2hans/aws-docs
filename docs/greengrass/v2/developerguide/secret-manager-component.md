---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/secret-manager-component.html
---

# Secret manager
<a name="secret-manager-component"></a>

The secret manager component (`aws.greengrass.SecretManager`) deploys secrets from AWS Secrets Manager to Greengrass core devices. Use this component to securely use credentials, such as passwords, in custom components on your Greengrass core devices. For more information about Secrets Manager, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

To access this component's secrets in your custom Greengrass components, use the [GetSecretValue](ipc-secret-manager.md#ipc-operation-getsecretvalue) operation in the AWS IoT Device SDK. For more information, see [Use the AWS IoT Device SDK to communicate with the Greengrass nucleus, other components, and AWS IoT CoreCommunicate with the Greengrass nucleus, other components, and AWS IoT Core](interprocess-communication.md) and [Retrieve secret values](ipc-secret-manager.md).

This component encrypts secrets on the core device to keep your credentials and passwords secure until you need to use them. It uses the core device's private key to encrypt and decrypt secrets.

**Topics**
+ [Versions](#secret-manager-component-versions)
+ [Type](#secret-manager-component-type)
+ [Operating system](#secret-manager-component-os-support)
+ [Requirements](#secret-manager-component-requirements)
+ [Dependencies](#secret-manager-component-dependencies)
+ [Configuration](#secret-manager-component-configuration)
+ [Local log file](#secret-manager-component-log-file)
+ [Changelog](#secret-manager-component-changelog)

## Versions
<a name="secret-manager-component-versions"></a>

This component has the following versions:
+ 2.2.x
+ 2.1.x
+ 2.0.x

## Type
<a name="secret-manager-component-type"></a>

<a name="public-component-type-plugin-para1"></a>This component is a plugin component (`aws.greengrass.plugin`). The [Greengrass nucleus](greengrass-nucleus-component.md) runs this component in the same Java Virtual Machine (JVM) as the nucleus. The nucleus restarts when you change this component's version on the core device.

<a name="public-component-type-plugin-para2"></a>This component uses the same log file as the Greengrass nucleus. For more information, see [Monitor AWS IoT Greengrass logs](monitor-logs.md).

<a name="public-component-type-more-information"></a>For more information, see [Component types](develop-greengrass-components.md#component-types).

## Operating system
<a name="secret-manager-component-os-support"></a>

This component can be installed on core devices that run the following operating systems:
+ Linux
+ Windows

## Requirements
<a name="secret-manager-component-requirements"></a>

This component has the following requirements:
+ The [Greengrass device role](device-service-role.md) must allow the `secretsmanager:GetSecretValue` action, as shown in the following example IAM policy.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Action": [
          "secretsmanager:GetSecretValue"
        ],
        "Effect": "Allow",
        "Resource": [
        "arn:{{aws}}:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:MySecret"
        ]
      }
    ]
  }
  ```

------

  ```
  ```
**Note**
If you use a customer-managed AWS Key Management Service key to encrypt secrets, the device role must also allow the `kms:Decrypt` action.

  For more information about IAM policies for Secrets Manager, see the following in the *AWS Secrets Manager User Guide*:
  + [Authentication and access control for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html)
  + [Actions, resources, and context keys you can use in an IAM policy or secret policy for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html)
+ Custom components must define an authorization policy that allows `aws.greengrass#GetSecretValue` to get secrets that you store with this component. In this authorization policy, you can restrict components' access to specific secrets. For more information, see [secret manager IPC authorization](ipc-secret-manager.md#ipc-secret-manager-authorization).
+ (Optional) If you store the core device's private key and certificate in a [hardware security module](hardware-security.md) (HSM), the HSM must support RSA keys, the private key must have the `unwrap` permission, and the public key must have the `wrap` permission.

### Endpoints and ports
<a name="secret-manager-component-endpoints"></a>

This component must be able to perform outbound requests to the following endpoints and ports, in addition to endpoints and ports required for basic operation. For more information, see [Allow device traffic through a proxy or firewall](allow-device-traffic.md).

| Endpoint | Port | Required | Description |
| --- | --- | --- | --- |
| `secretsmanager.{{region}}.amazonaws.com` | 443 | Yes | Download secrets to the core device. |

## Dependencies
<a name="secret-manager-component-dependencies"></a>

When you deploy a component, AWS IoT Greengrass also deploys compatible versions of its dependencies. This means that you must meet the requirements for the component and all of its dependencies to successfully deploy the component. This section lists the dependencies for the [released versions](#secret-manager-component-changelog) of this component and the semantic version constraints that define the component versions for each dependency. You can also view the dependencies for each version of the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com//greengrass). On the component details page, look for the **Dependencies** list.

------
#### [ 2.2.7 ]

The following table lists the dependencies for version 2.2.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.17.0 | Soft |

------
#### [ 2.2.6 ]

The following table lists the dependencies for version 2.2.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.16.0 | Soft |

------
#### [ 2.2.2 – 2.2.5 ]

The following table lists the dependencies for versions 2.2.2 through 2.2.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.15.0 | Soft |

------
#### [ 2.2.0 ]

The following table lists the dependencies for versions 2.2.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.13.0 <2.14.0 | Soft |

------
#### [ 2.1.7 – 2.1.8 ]

The following table lists the dependencies for versions 2.1.7 and 2.1.8 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.13.0 | Soft |

------
#### [ 2.1.6 ]

The following table lists the dependencies for version 2.1.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.12.0 | Soft |

------
#### [ 2.1.5 ]

The following table lists the dependencies for version 2.1.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.11.0 | Soft |

------
#### [ 2.1.4 ]

The following table lists the dependencies for version 2.1.4 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.10.0 | Soft |

------
#### [ 2.1.3 ]

The following table lists the dependencies for version 2.1.3 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.9.0 | Soft |

------
#### [ 2.1.2 ]

The following table lists the dependencies for version 2.1.2 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.8.0 | Soft |

------
#### [ 2.1.1 ]

The following table lists the dependencies for version 2.1.1 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.7.0 | Soft |

------
#### [ 2.1.0 ]

The following table lists the dependencies for version 2.1.0 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) | >=2.5.0 <2.6.0 | Soft |

------
#### [ 2.0.9 ]

The following table lists the dependencies for version 2.0.9 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.5.0  | Soft |

------
#### [ 2.0.8 ]

The following table lists the dependencies for version 2.0.8 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.4.0  | Soft |

------
#### [ 2.0.7 ]

The following table lists the dependencies for version 2.0.7 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.3.0  | Soft |

------
#### [ 2.0.6 ]

The following table lists the dependencies for version 2.0.6 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.0 <2.2.0  | Soft |

------
#### [ 2.0.4 and 2.0.5 ]

The following table lists the dependencies for versions 2.0.4 and 2.0.5 of this component.

| Dependency | Compatible versions | Dependency type |
| --- | --- | --- |
| [Greengrass nucleus](greengrass-nucleus-component.md) |  >=2.0.3 <2.1.0  | Soft |

------

For more information about component dependencies, see the [component recipe reference](component-recipe-reference.md#recipe-reference-component-dependencies).

## Configuration
<a name="secret-manager-component-configuration"></a>

This component provides the following configuration parameters that you can customize when you deploy the component.

`periodicRefreshIntervalMin` (optional)
The interval in minutes where this component syncs the configured secrets on the core device with the latest secret values from the AWS Secrets Manager service. If this interval is not configured, secret manager will not refresh the configured secrets periodically.

```
{
  "cloudSecrets": [
    {
      "arn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyGreengrassSecret-abcdef"
    }
  ],
  "periodicRefreshIntervalMin" : 60
}
```

`cloudSecrets`
A list of Secrets Manager secrets to deploy to the core device. You can specify labels to define which versions of each secret to deploy. If you don't specify a version, this component deploys the version with the staging label `AWSCURRENT` attached. For more information, see [Staging labels](https://docs.aws.amazon.com/secretsmanager/latest/userguide/terms-concepts.html#term_staging-label) in the *AWS Secrets Manager User Guide*.
The secret manager component caches secrets locally. If the secret value changes in Secrets Manager, this component doesn't automatically retrieve the new value. To update the local copy, give the secret a new label and configure this component to retrieve the secret identified by the new label.
Each object contains the following information:
`arn`
The ARN of the secret to deploy. The ARN of the secret can either be a full ARN or a partial ARN. We recommend that you specify a complete ARN rather than a partial ARN. For more information, see [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen). The following is an example of a full ARN and a partial ARN:
+ Full ARN: `arn:aws:secretsmanager:us-east-2:111122223333:secret:{{SecretName}}-abcdef`
+ Partial ARN: `arn:aws:secretsmanager:us-east-2:111122223333:secret:{{SecretName}}`
`labels`
(Optional) A list of labels to identify the versions of the secret to deploy to the core device.
Each label must be a string.

**Example: Configuration merge update**

```
{
  "cloudSecrets": [
    {
      "arn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyGreengrassSecret-abcdef"
    }
  ]
}
```

## Local log file
<a name="secret-manager-component-log-file"></a>

This component uses the same log file as the [Greengrass nucleus](greengrass-nucleus-component.md) component.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/greengrass.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\greengrass.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/greengrass.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\greengrass.log -Tail 10 -Wait
  ```

------

## Changelog
<a name="secret-manager-component-changelog"></a>

The following table describes the changes in each version of the component.

|  **Version**  |  **Changes**  |
| --- | --- |
| 2.2.9 |  **Bug fixes and improvements**<br />   General bug fixes and improvements.     |
| 2.2.8 | Updates the component version for the Greengrass nucleus version 2.17.0 release. |
| 2.2.7 | Version updated for Greengrass nucleus version 2.16.0 release. |
| 2.2.6 |  **Bug fixes and improvements**<br /> Fixes an issue where secret manager fails to get a secret due to a slow or unresponsive Trusted Platform Module. <br />Version updated for Greengrass nucleus version 2.15.0 release.   |
| 2.2.5 |  **Bug fixes and improvements**<br /> Fixes an issue where a secret doesn't get fetched from the AWS Cloud if it isn't present in the local cache.   |
| 2.2.4 |  **Bug fixes and improvements**<br /> Reduces the frequency of writes to the local secret store. Secret manager now writes to the local store only when secrets are updated.   |
| 2.2.3 |  **Bug fixes and improvements**<br /> Fixes an issue where secret manager wipes the locally persisted secrets when the core device is offline and the device’s security service (such as an HSM) is unavailable.   |
| 2.2.2 |  **Bug fixes and improvements**<br /> Fixes an issue where secret manager doesn’t download the secrets configured with partial arns.   |
| 2.2.1 |  **Bug fixes and improvements**<br /> Supports secret manager on Nucleus versions 2.5.0 and above.   |
| 2.2.0 |  **New features**<br /> Adds support for periodic refresh of the configured secrets through a new component configuration key. <br />Adds support for a new request parameter in the `GetSecretValue` IPC request to refresh the secrets per request   |
| 2.1.8 |  **Bug fixes and improvements**<br /> Fixes an issue where secret manager doesn't accept a partial arn.   |
| 2.1.7 | Version updated for Greengrass nucleus version 2.12.0 release. |
| 2.1.6 | Version updated for Greengrass nucleus version 2.11.0 release. |
| 2.1.5 | Version updated for Greengrass nucleus version 2.10.0 release. |
| 2.1.4 |  **Bug fixes and improvements**<br /> Fixes an issue where cached secrets were being removed when secret manager is deployed and Greengrass nucleus restarts. <br />Version updated for Greengrass nucleus version 2.9.0 release.   |
| 2.1.3 | Version updated for Greengrass nucleus version 2.8.0 release. |
| 2.1.2 | Version updated for Greengrass nucleus version 2.7.0 release. |
| 2.1.1 | Version updated for Greengrass nucleus version 2.6.0 release. |
| 2.1.0 |  **New features**<br />   Adds support for hardware security integration. The secret manager component can encrypt and decrypt secrets using a private key that you store in a hardware security module (HSM). For more information, see [Hardware security integration](hardware-security.md).   <br />**Bug fixes and improvements**<br />   Version updated for Greengrass nucleus version 2.5.0 release.     |
| 2.0.9 | Version updated for Greengrass nucleus version 2.4.0 release. |
| 2.0.8 | Version updated for Greengrass nucleus version 2.3.0 release. |
| 2.0.7 | Version updated for Greengrass nucleus version 2.2.0 release. |
| 2.0.6 | Version updated for Greengrass nucleus version 2.1.0 release. |
| 2.0.5 |  **Improvements**<br />   Add support for AWS China Regions and AWS GovCloud (US) Regions.     |
| 2.0.4 | Initial version. |
