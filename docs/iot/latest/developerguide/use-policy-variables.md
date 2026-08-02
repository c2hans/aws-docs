---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html
---

# Using X.509 certificate policy variables
<a name="use-policy-variables"></a>

This topic provides details of how to use certificate policy variables. X.509 certificate policy variables are essential when you create AWS IoT Core policies that give permissions based on X.509 certificate attributes. If your X.509 certificate doesn't include a particular certificate attribute but the corresponding certificate policy variable is used in your policy document, the policy evaluation might lead to unexpected behavior. This is because the missing policy variable doesn't get evaluated in the policy statement.

**Topics**
+ [X.509 certificate example](#certificate-example)
+ [Using certificate issuer attributes as certificate policy variables](#issuer-attributes-policy)
+ [Using certificate subject attributes as certificate policy variables](#subject-attributes-policy)
+ [Using certificate Issuer alternate name attributes as certificate policy variables](#issuer-alternate-name-attributes-policy)
+ [Using certificate subject alternate name attributes as certificate policy variables](#subject-alternate-name-attributes-policy)
+ [Using other certificate attribute as a certificate policy variable](#other-attributes-policy)
+ [X.509 Certificate policy variable limitations](#policy-limits)
+ [Example policies using certificate policy variables](#example-attributes-policy)

## X.509 certificate example
<a name="certificate-example"></a>

A typical X.509 certificate might appear as follows. This example certificate includes certificate attributes. During the evaluation of AWS IoT Core policies, the following certificate attributes will be populated as certificate policy variables: `Serial Number`, `Issuer`, `Subject`, `X509v3 Issuer Alternative Name`, and `X509v3 Subject Alternative Name`.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            92:12:85:cb:b7:a5:e0:86
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=IoT Devices, OU=SmartHome, ST=WA, CN=IoT Devices Primary CA,
				GN=Primary CA1/initials=XY/dnQualifier=Example corp,
				SN=SmartHome/ title=CA1/pseudonym=Primary_CA/generationQualifier=2/serialNumber=987
        Validity
            Not Before: Mar 26 03:25:40 2024 GMT
            Not After : Apr 28 03:25:40 2025 GMT
        Subject: C=US, O=IoT Devices, OU=LightBulb, ST=NY, CN=LightBulb Device Cert,
				GN=Bulb/initials=ZZ/dnQualifier=Bulb001,
				SN=Multi Color/title=RGB/pseudonym=RGB Device/generationQualifier=4/serialNumber=123
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    << REDACTED >>
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Key Usage:
                Digital Signature, Non Repudiation, Key Encipherment
            X509v3 Subject Alternative Name:
                DNS:example.com, IP Address:1.2.3.4, URI:ResourceIdentifier001, email:device1@example.com, DirName:/C=US/O=IoT/OU=SmartHome/CN=LightBulbCert
            X509v3 Issuer Alternative Name:
                DNS:issuer.com, IP Address:5.6.7.8, URI:PrimarySignerCA, email:primary@issuer.com, DirName:/C=US/O=Issuer/OU=IoT Devices/CN=Primary Issuer CA
    Signature Algorithm: sha256WithRSAEncryption
         << REDACTED >>
```

## Using certificate issuer attributes as certificate policy variables
<a name="issuer-attributes-policy"></a>

The following table provides details of how certificate issuer attributes will be populated in an AWS IoT Core policy.

**Issuer attributes to be populated in a policy**

| Certificate issuer attributes | Certificate policy variables |
| --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |

## Using certificate subject attributes as certificate policy variables
<a name="subject-attributes-policy"></a>

The following table provides details of how certificate subject attributes will be populated in an AWS IoT Core policy.

**Subject attributes to be populated in a policy**

| Certificate subject attributes | Certificate policy variables |
| --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |

## Using certificate Issuer alternate name attributes as certificate policy variables
<a name="issuer-alternate-name-attributes-policy"></a>

The following table provides details of how certificate issuer alternate name attributes will be populated in an AWS IoT Core policy.

**Issuer alternate name attributes to be populated in a policy**

| X509v3 Issuer Alternative Name | Attribute in a policy |
| --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |

## Using certificate subject alternate name attributes as certificate policy variables
<a name="subject-alternate-name-attributes-policy"></a>

The following table provides details of how certificate subject alternate name attributes will be populated in an AWS IoT Core policy.

**Subject alternate name attributes to be populated in a policy**

| X509v3 Subject Alternative Name | Attribute in a policy |
| --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html)  |

## Using other certificate attribute as a certificate policy variable
<a name="other-attributes-policy"></a>

The following table provides details of how other certificate attributes will be populated in an AWS IoT Core policy.

**Other attributes to be populated in a policy**

| Other certificate attribute | Certificate policy variable |
| --- | --- |
| `Serial Number: 92:12:85:cb:b7:a5:e0:86` | `iot:Certificate.SerialNumber = 10525622389124227206` |

## X.509 Certificate policy variable limitations
<a name="policy-limits"></a>

The following limitations apply to X.509 certificate policy variables:

Missing policy variables
If your X.509 certificate doesn't include a particular certificate attribute but the corresponding certificate policy variable is used in your policy document, the policy evaluation might lead to unexpected behavior. This is because the missing policy variable doesn't get evaluated in the policy statement.

Certificate SerialNumber format
AWS IoT Core treats the certificate serial number as the string representation of a decimal integer. For example, if a policy only allows connections with Client ID matching the certificate serial number, the client ID must be the serial number in decimal format.

Wildcards
If wildcard characters are present in certificate attributes, the policy variable is not replaced by the certificate attribute value. This will leave the `${policy-variable}` text in the policy document. This might cause authorization failure. The following wildcard characters can be used: `*`, `$`, `+`, `?`, and `#`.

Array fields
Certificate attributes that contain arrays are limited to five items. Additional items are ignored.

String length
All string values are limited to 1024 characters. If a certificate attribute contains a string longer than 1024 characters, the policy variable is not replaced by the certificate attribute value. This will leave the `${policy-variable}` in the policy document. This might cause authorization failure.

Special Characters
Any special character, such as `,`, `"`, `\`, `+`, `=`, `<`, `>` and `;` must be prefixed with a backslash (`\`) when used in a policy variable. For example, `Amazon Web Services O=Amazon.com Inc. L=Seattle ST=Washington C=US` becomes `Amazon Web Service O\=Amazon.com Inc. L\=Seattle ST\=Washington C\=US`.

## Example policies using certificate policy variables
<a name="example-attributes-policy"></a>

The following policy document allows connections with client ID that matches the certificate serial number and publishing to the topic that matches the pattern: `${iot:Certificate.Subject.Organization}/device-stats/${iot:ClientId}/*`.

**Important**
If your X.509 certificate doesn't include a particular certificate attribute but the corresponding certificate policy variable is used in your policy document, the policy evaluation might lead to unexpected behavior. This is because the missing policy variable doesn't get evaluated in the policy statement. For example, if you attach the following policy document to a certificate that doesn't contain the `iot:Certificate.Subject.Organization` attribute, the `iot:Certificate.Subject.Organization` certificate policy variables won't be populated during the policy evaluation.

****

```
{
	"Version":"2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"iot:Connect"
			],
			"Resource": [
				"arn:aws:iot:us-east-1:123456789012:client/${iot:Certificate.SerialNumber}"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"iot:Publish"
			],
			"Resource": [
				"arn:aws:iot:us-east-1:123456789012:topic/${iot:Certificate.Subject.Organization}/device-stats/${iot:ClientId}/*"
			]
		}
	]
}
```

You can also use the [Null condition operator](https://docs.aws.amazon.com//IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_Null) to ensure that the certificate policy variables used in a policy are populated during policy evaluation. The following policy document allows `iot:Connect` with certificates only when the Certificate Serial Number and Certificate Subject Common name attributes are present.

All of the certificate policy variables have String values, so all of the [String condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String) are supported.

****

```
{
	"Version":"2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"iot:Connect"
			],
			"Resource": [
				"arn:aws:iot:us-east-1:123456789012:client/*"
			],
			"Condition": {
				"Null": {
					"iot:Certificate.SerialNumber": "false",
					"iot:Certificate.Subject.CommonName": "false"
				}
			}
		}
	]
}
```
