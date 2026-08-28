---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcaconnectorscep-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorSCEP::Connector
<a name="aws-resource-pcaconnectorscep-connector"></a>

Connector for SCEP is a service that links AWS Private Certificate Authority to your SCEP-enabled devices. The connector brokers the exchange of certificates from AWS Private CA to your SCEP-enabled devices and mobile device management systems. The connector is a complex type that contains the connector's configuration settings.

## Syntax
<a name="aws-resource-pcaconnectorscep-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcaconnectorscep-connector-syntax.json"></a>

```
{
  "Type" : "AWS::PCAConnectorSCEP::Connector",
  "Properties" : {
      "[CertificateAuthorityArn](#cfn-pcaconnectorscep-connector-certificateauthorityarn)" : {{String}},
      "[MobileDeviceManagement](#cfn-pcaconnectorscep-connector-mobiledevicemanagement)" : {{MobileDeviceManagement}},
      "[Tags](#cfn-pcaconnectorscep-connector-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[VpcEndpointId](#cfn-pcaconnectorscep-connector-vpcendpointid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pcaconnectorscep-connector-syntax.yaml"></a>

```
Type: AWS::PCAConnectorSCEP::Connector
Properties:
  [CertificateAuthorityArn](#cfn-pcaconnectorscep-connector-certificateauthorityarn): {{String}}
  [MobileDeviceManagement](#cfn-pcaconnectorscep-connector-mobiledevicemanagement): {{
    MobileDeviceManagement}}
  [Tags](#cfn-pcaconnectorscep-connector-tags): {{
    {{Key}}: {{Value}}}}
  [VpcEndpointId](#cfn-pcaconnectorscep-connector-vpcendpointid): {{String}}
```

## Properties
<a name="aws-resource-pcaconnectorscep-connector-properties"></a>

`CertificateAuthorityArn`  <a name="cfn-pcaconnectorscep-connector-certificateauthorityarn"></a>
The Amazon Resource Name (ARN) of the certificate authority associated with the connector.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:acm-pca:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MobileDeviceManagement`  <a name="cfn-pcaconnectorscep-connector-mobiledevicemanagement"></a>
Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure `MobileDeviceManagement`, then the connector is for general-purpose use and this object is empty.
*Required*: No
*Type*: [MobileDeviceManagement](aws-properties-pcaconnectorscep-connector-mobiledevicemanagement.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-pcaconnectorscep-connector-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointId`  <a name="cfn-pcaconnectorscep-connector-vpcendpointid"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-pcaconnectorscep-connector-return-values"></a>

### Ref
<a name="aws-resource-pcaconnectorscep-connector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-pcaconnectorscep-connector-return-values-fn--getatt"></a>

####
<a name="aws-resource-pcaconnectorscep-connector-return-values-fn--getatt-fn--getatt"></a>

`ConnectorArn`  <a name="ConnectorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connector.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The connector's HTTPS public SCEP URL.

`Type`  <a name="Type-fn::getatt"></a>
The connector type.

## Examples
<a name="aws-resource-pcaconnectorscep-connector--examples"></a>

**Topics**
+ [Create a general-purpose SCEP connector and challenge resource](#aws-resource-pcaconnectorscep-connector--examples--Create_a_general-purpose_SCEP_connector_and_challenge_resource)
+ [Create connector to use with Microsoft Intune](#aws-resource-pcaconnectorscep-connector--examples--Create_connector_to_use_with_Microsoft_Intune)

### Create a general-purpose SCEP connector and challenge resource
<a name="aws-resource-pcaconnectorscep-connector--examples--Create_a_general-purpose_SCEP_connector_and_challenge_resource"></a>

The following example creates a AWS Private Certificate Authority (CA) general-purpose connector with a challenge password. Before you create a connector, you must complete a few prerequisites, including creating a private CA in AWS Private Certificate Authority (CA). For more information, see [Set up Connector for SCEP](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-setting-up.html).

#### JSON
<a name="aws-resource-pcaconnectorscep-connector--examples--Create_a_general-purpose_SCEP_connector_and_challenge_resource--json"></a>

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "Cloudformation template to set up a general-purpose connector for SCEP and challenge password.",
   "Resources": {
      "RootCA": {
         "Type": "AWS::ACMPCA::CertificateAuthority",
         "Properties": {
         "Type": "ROOT",
         "KeyAlgorithm": "RSA_2048",
         "SigningAlgorithm": "SHA256WITHRSA",
         "Subject": {
            "Country": "US",
            "Organization": "string",
            "OrganizationalUnit": "string",
            "DistinguishedNameQualifier": "string",
            "State": "string",
            "CommonName": "123",
            "SerialNumber": "string",
            "Locality": "string",
            "Title": "string",
            "Surname": "string",
            "GivenName": "string",
            "Initials": "DG",
            "Pseudonym": "string",
            "GenerationQualifier": "DBG"
         },
         "RevocationConfiguration": {
            "CrlConfiguration": {
               "Enabled": false
            }
         }
         }
      },
      "RootCACertificate": {
         "Type": "AWS::ACMPCA::Certificate",
         "Properties": {
         "CertificateAuthorityArn": {
            "Fn::Ref": "RootCA"
         },
         "CertificateSigningRequest": {
            "Fn::GetAtt": [
               "RootCA",
               "CertificateSigningRequest"
            ]
         },
         "SigningAlgorithm": "SHA256WITHRSA",
         "TemplateArn": "arn:aws:acm-pca:::template/RootCACertificate/V1",
         "Validity": {
            "Type": "YEARS",
            "Value": 100
         }
         }
      },
      "RootCAActivation": {
         "Type": "AWS::ACMPCA::CertificateAuthorityActivation",
         "Properties": {
         "CertificateAuthorityArn": {
            "Fn::Ref": "RootCA"
         },
         "Certificate": {
            "Fn::GetAtt": [
               "RootCACertificate",
               "Certificate"
            ]
         },
         "Status": "ACTIVE"
         }
      },
      "RootCAResourceShare": {
         "DependsOn": "RootCAActivation",
         "Type": "AWS::RAM::ResourceShare",
         "Properties": {
         "Name": "RootCAResourceShare",
         "PermissionArns": [
            "arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority"
         ],
         "ResourceArns": [
            {
               "Fn::Ref": "RootCA"
            }
         ],
         "Sources": [
            {
               "Fn::Ref": "AWS::AccountId"
            }
         ],
         "Principals": [
            "pca-connector-scep.amazonaws.com"
         ]
         }
      },
      "GeneralPurposeConnector": {
         "DependsOn": "RootCAResourceShare",
         "Type": "AWS::PCAConnectorSCEP::Connector",
         "Properties": {
         "CertificateAuthorityArn": {
            "Fn::Ref": "RootCA"
         }
         }
      },
      "GeneralPurposeConnectorChallenge": {
         "DependsOn": "GeneralPurposeConnector",
         "Type": "AWS::PCAConnectorSCEP::Challenge",
         "Properties": {
         "ConnectorArn": {
            "Fn::Ref": "GeneralPurposeConnector"
         }
         }
      }
   },
   "Outputs": {
      "GeneralPurposeConnector": {
         "Value": {
         "Fn::Ref": "GeneralPurposeConnector"
         }
      },
      "GeneralPurposeConnectorChallenge": {
         "Value": {
         "Fn::Ref": "GeneralPurposeConnectorChallenge"
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-pcaconnectorscep-connector--examples--Create_a_general-purpose_SCEP_connector_and_challenge_resource--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Cloudformation template to set up a general-purpose connector for SCEP and challenge password.
Resources:
   RootCA:
      Type: AWS::ACMPCA::CertificateAuthority
      Properties:
      Type: ROOT
      KeyAlgorithm: RSA_2048
      SigningAlgorithm: SHA256WITHRSA
      Subject:
         Country: US
         Organization: string
         OrganizationalUnit: string
         DistinguishedNameQualifier: string
         State: string
         CommonName: '123'
         SerialNumber: string
         Locality: string
         Title: string
         Surname: string
         GivenName: string
         Initials: DG
         Pseudonym: string
         GenerationQualifier: DBG
      RevocationConfiguration:
         CrlConfiguration:
            Enabled: false
   RootCACertificate:
      Type: AWS::ACMPCA::Certificate
      Properties:
      CertificateAuthorityArn: !Ref RootCA
      CertificateSigningRequest: !GetAtt RootCA.CertificateSigningRequest
      SigningAlgorithm: SHA256WITHRSA
      TemplateArn: arn:aws:acm-pca:::template/RootCACertificate/V1
      Validity:
         Type: YEARS
         Value: 100
   RootCAActivation:
      Type: AWS::ACMPCA::CertificateAuthorityActivation
      Properties:
      CertificateAuthorityArn: !Ref RootCA
      Certificate: !GetAtt RootCACertificate.Certificate
      Status: ACTIVE
   RootCAResourceShare:
      DependsOn: RootCAActivation
      Type: AWS::RAM::ResourceShare
      Properties:
      Name: RootCAResourceShare
      PermissionArns:
         - arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority
      ResourceArns:
         - !Ref RootCA
      Sources:
         - !Ref AWS::AccountId
      Principals:
         - pca-connector-scep.amazonaws.com
   GeneralPurposeConnector:
      DependsOn: RootCAResourceShare
      Type: AWS::PCAConnectorSCEP::Connector
      Properties:
      CertificateAuthorityArn: !Ref RootCA
   GeneralPurposeConnectorChallenge:
      DependsOn: GeneralPurposeConnector
      Type: AWS::PCAConnectorSCEP::Challenge
      Properties:
      ConnectorArn: !Ref GeneralPurposeConnector
Outputs:
   GeneralPurposeConnector:
      Value: !Ref GeneralPurposeConnector
   GeneralPurposeConnectorChallenge:
      Value: !Ref GeneralPurposeConnectorChallenge
```

### Create connector to use with Microsoft Intune
<a name="aws-resource-pcaconnectorscep-connector--examples--Create_connector_to_use_with_Microsoft_Intune"></a>

The following example creates a AWS Private Certificate Authority (CA) connector to use with Microsoft Intune. Before you create a connector, you must complete a few prerequisites, including creating a private CA in AWS Private Certificate Authority (CA). For more information, see [Set up Connector for SCEP](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep-setting-up.html).

#### JSON
<a name="aws-resource-pcaconnectorscep-connector--examples--Create_connector_to_use_with_Microsoft_Intune--json"></a>

```
{
      "AWSTemplateFormatVersion": "2010-09-09",
      "Description": "Cloudformation template to set up a connector to use with Microsoft Intune.",
      "Resources": {
         "RootCA": {
            "Type": "AWS::ACMPCA::CertificateAuthority",
            "Properties": {
            "Type": "ROOT",
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
               "Country": "US",
               "Organization": "string",
               "OrganizationalUnit": "string",
               "DistinguishedNameQualifier": "string",
               "State": "string",
               "CommonName": "123",
               "SerialNumber": "string",
               "Locality": "string",
               "Title": "string",
               "Surname": "string",
               "GivenName": "string",
               "Initials": "DG",
               "Pseudonym": "string",
               "GenerationQualifier": "DBG"
            },
            "RevocationConfiguration": {
               "CrlConfiguration": {
                  "Enabled": false
               }
            }
            }
         },
         "RootCACertificate": {
            "Type": "AWS::ACMPCA::Certificate",
            "Properties": {
            "CertificateAuthorityArn": {
               "Fn::Ref": "RootCA"
            },
            "CertificateSigningRequest": {
               "Fn::GetAtt": [
                  "RootCA",
                  "CertificateSigningRequest"
               ]
            },
            "SigningAlgorithm": "SHA256WITHRSA",
            "TemplateArn": "arn:aws:acm-pca:::template/RootCACertificate/V1",
            "Validity": {
               "Type": "YEARS",
               "Value": 100
            }
            }
         },
         "RootCAActivation": {
            "Type": "AWS::ACMPCA::CertificateAuthorityActivation",
            "Properties": {
            "CertificateAuthorityArn": {
               "Fn::Ref": "RootCA"
            },
            "Certificate": {
               "Fn::GetAtt": [
                  "RootCACertificate",
                  "Certificate"
               ]
            },
            "Status": "ACTIVE"
            }
         },
         "RootCAResourceShare": {
            "DependsOn": "RootCAActivation",
            "Type": "AWS::RAM::ResourceShare",
            "Properties": {
            "Name": "RootCAResourceShare",
            "PermissionArns": [
               "arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority"
            ],
            "ResourceArns": [
               {
                  "Fn::Ref": "RootCA"
               }
            ],
            "Sources": [
               {
                  "Fn::Ref": "AWS::AccountId"
               }
            ],
            "Principals": [
               "pca-connector-scep.amazonaws.com"
            ]
            }
         },
         "IntuneConnector": {
            "DependsOn": "RootCAResourceShare",
            "Type": "AWS::PCAConnectorSCEP::Connector",
            "Properties": {
            "CertificateAuthorityArn": {
               "Fn::Ref": "RootCA"
            },
            "MobileDeviceManagement": {
               "Intune": {
                  "AzureApplicationId": "222-222-222-222-222",
                  "Domain": "example.onmicrosoft.com"
               }
            }
            }
         }
      },
      "Outputs": {
         "IntuneConnector": {
            "Value": {
            "Fn::Ref": "IntuneConnector"
            }
         }
      }
   }
```

#### YAML
<a name="aws-resource-pcaconnectorscep-connector--examples--Create_connector_to_use_with_Microsoft_Intune--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Cloudformation template to set up a connector to use with Microsoft Intune.
Resources:
   RootCA:
      Type: AWS::ACMPCA::CertificateAuthority
      Properties:
      Type: ROOT
      KeyAlgorithm: RSA_2048
      SigningAlgorithm: SHA256WITHRSA
      Subject:
         Country: US
         Organization: string
         OrganizationalUnit: string
         DistinguishedNameQualifier: string
         State: string
         CommonName: '123'
         SerialNumber: string
         Locality: string
         Title: string
         Surname: string
         GivenName: string
         Initials: DG
         Pseudonym: string
         GenerationQualifier: DBG
      RevocationConfiguration:
         CrlConfiguration:
            Enabled: false
   RootCACertificate:
      Type: AWS::ACMPCA::Certificate
      Properties:
      CertificateAuthorityArn: !Ref RootCA
      CertificateSigningRequest: !GetAtt RootCA.CertificateSigningRequest
      SigningAlgorithm: SHA256WITHRSA
      TemplateArn: arn:aws:acm-pca:::template/RootCACertificate/V1
      Validity:
         Type: YEARS
         Value: 100
   RootCAActivation:
      Type: AWS::ACMPCA::CertificateAuthorityActivation
      Properties:
      CertificateAuthorityArn: !Ref RootCA
      Certificate: !GetAtt RootCACertificate.Certificate
      Status: ACTIVE
   RootCAResourceShare:
      DependsOn: RootCAActivation
      Type: AWS::RAM::ResourceShare
      Properties:
      Name: RootCAResourceShare
      PermissionArns:
         - arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority
      ResourceArns:
         - !Ref RootCA
      Sources:
         - !Ref AWS::AccountId
      Principals:
         - pca-connector-scep.amazonaws.com
   IntuneConnector:
      DependsOn: RootCAResourceShare
      Type: AWS::PCAConnectorSCEP::Connector
      Properties:
      CertificateAuthorityArn: !Ref RootCA
      MobileDeviceManagement:
         Intune:
            AzureApplicationId: "222-222-222-222-222"
            Domain: "example.onmicrosoft.com"
   Outputs:
   IntuneConnector:
      Value: !Ref IntuneConnector
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
