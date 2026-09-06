---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/module-parameters.html
---

# Module parameters
<a name="module-parameters"></a>

Managed VPC - Hub

```
Outputs:

- SSM parameter store
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PublicSubnet1/AZ
  - /Network/PublicSubnet1/SubnetID
  - /Network/PublicSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /Network/PublicSubnet2/AZ
  - /Network/PublicSubnet2/SubnetID
  - /Network/PublicSubnet2/RouteTableID
```

Managed VPC - Spoke

```
Inputs:

- SSM parameter store
  - /Core/MCSStack/Name
  - /Core/HubRegion
  - /Network/VpcId (Remote)
  - /Network/VpcCidr (Remote)

Outputs:

- SSM parameter store
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PublicSubnet1/AZ
  - /Network/PublicSubnet1/SubnetID
  - /Network/PublicSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /Network/PublicSubnet2/AZ
  - /Network/PublicSubnet2/SubnetID
  - /Network/PublicSubnet2/RouteTableID
```

Unmanaged VPC

```
Inputs:

- SSM Parameter Store
  - /Core/HubRegion
  - /Core/MCSStack/Name

Outputs:

- SSM Parameter Store
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PublicSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PublicSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PublicSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PublicSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PublicSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /Network/PublicSubnet2/RouteTableID
```

Managed Active Directory - Hub

```
Inputs:

- SSM Parameter Store
  - /Network/VpcId
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID

Outputs:

- SSM Parameter Store
  - /Identity/ActiveDirectoryId
  - /Identity/ActiveDirectoryServerIP1
  - /Identity/ActiveDirectoryServerIP2
  - /Identity/ActiveDirectoryDomainName
  - /Identity/McsModulesActiveDirectorySecretArn
- Secrets Manager
  - /Identity/DefaultAdminActiveDirectoryLoginCredentials
  - /Identity/StudioAdminActiveDirectoryLoginCredentials
  - /Identity/AdConnectorServiceAccountActiveDirectoryLoginCredentials
  - /Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials
```

Managed Active Directory - Spoke

```
Inputs:

- SSM Parameter Store
  - /Core/HubRegion
  - /Network/VpcId
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PrivateSubnet2/RouteTableID
  - /Network/VpcCidr (Remote)
  - /Identity/ActiveDirectoryId (Remote)
  - /Identity/ActiveDirectoryServerIP1 (Remote)
  - /Identity/ActiveDirectoryServerIP2 (Remote)
  - /Identity/ActiveDirectoryDomainName (Remote)
- Secrets Manager
  - /Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials (Remote)

Outputs:

- SSM Parameter Store
  - /Identity/ActiveDirectoryId
  - /Identity/ActiveDirectoryServerIP1
  - /Identity/ActiveDirectoryServerIP2
  - /Identity/ActiveDirectoryDomainName
  - /Identity/McsModulesActiveDirectorySecretArn
- Secrets Manager
  - /Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials
```

Unmanaged Active Directory

```
Outputs:

- SSM Parameter Store
  - /Identity/ActiveDirectoryId
  - /Identity/ActiveDirectoryServerIP1
  - /Identity/ActiveDirectoryServerIP2
  - /Identity/ActiveDirectoryDomainName
  - /Identity/McsModulesActiveDirectorySecretArn
  - /Identity/Region
- Secrets Manager
  - /Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials
```

Leostream Broker - Hub

```
Inputs:

- SSM Parameter Store
  - /Core/Tag/Key
  - /Core/Tag/Value/Linux
  - /Core/Tag/Value/Windows
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /Identity/ActiveDirectoryServerIP1
  - /Identity/ActiveDirectoryServerIP2
  - /Identity/ActiveDirectoryDomainName
  - /Identity/McsModulesActiveDirectorySecretArn

Outputs:

- SSM Parameter Store
  - /WorkstationManagement/Leostream/DNSName
  - /WorkstationManagement/CustomResource/AmiAutomationLambda/ARN
  - /WorkstationManagement/ImageBuilder/InstanceProfile/Name
  - /WorkstationManagement/Leostream/Database/Credentials
  - /WorkstationManagement/Workstation/Windows/AMI-Id
  - /WorkstationManagement/Workstation/Linux/AMI-Id
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/Leostream/BrokerInstanceRoleArn
  - /WorkstationManagement/Leostream/RDS/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/Leostream/BrokerHostedZoneId
  - /WorkstationManagement/Leostream/BrokerHostedZoneId
  - /WorkstationManagement/Leostream/BrokerSecurityGroupId
  - /WorkstationManagement/WorkstationSecurityGroupId
  - /WorkstationManagement/Leostream/DatabaseSecurityGroupId
  - /WorkstationManagement/Workstation/Windows/AMI-Deployed
  - /WorkstationManagement/Workstation/Linux/AMI-Deployed
  - /WorkstationManagement/Leostream/BrokerLoadBalancerArn
  - /WorkstationManagement/Leostream/BrokerLoadBalancerSecurityGroupId
  - /WorkstationManagement/Leostream/BrokerHttpsListenerArn
- Secrets Manager
  - /WorkstationManagement/Leostream/Console/AdminUserCredentials
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials
```

Leostream Broker - Spoke

```
Inputs:

- SSM Parameter Store
  - /Core/HubRegion
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /Identity/ActiveDirectoryServerIP1
  - /Identity/ActiveDirectoryServerIP2
  - /Identity/ActiveDirectoryDomainName
  - /Identity/ActiveDirectorySecretArn
  - /WorkstationManagement/Leostream/DNSName (Remote)
  - /WorkstationManagement/ImageBuilder/InstanceProfile/Name (Remote)
  - /WorkstationManagement/Workstation/Windows/AMI-Id (Remote)
  - /WorkstationManagement/Workstation/Linux/AMI-Id (Remote)
  - /WorkstationManagement/Leostream/BrokerInstanceRoleArn (Remote)
  - /WorkstationManagement/Leostream/BrokerSecurityGroupId (Remote)
  - /WorkstationManagement/WorkstationSecurityGroupId (Remote)
  - /WorkstationManagement/Leostream/DatabaseSecurityGroupId (Remote)
  - /WorkstationManagement/Workstation/Windows/AMI-Deployed (Remote)
  - /WorkstationManagement/Workstation/Linux/AMI-Deployed (Remote)
  - /WorkstationManagement/Leostream/BrokerHostedZoneId (Remote)
- Secrets Manager
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials (Remote)
  - /WorkstationManagement/Leostream/Database/Credentials (Remote)
  - /WorkstationManagement/Leostream/Console/AdminUserCredentials (Remote)

Outputs

- SSM Parameter Store
  - /WorkstationManagement/Leostream/DNSName
  - /WorkstationManagement/ImageBuilder/InstanceProfile/Name
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/Leostream/RDS/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/Leostream/Console/AdminUserCredentials/SecretArn
- Secrets Manager
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials
  - /WorkstationManagement/Leostream/Database/Credentials
  - /WorkstationManagement/Leostream/Console/AdminUserCredentials
```

Leostream Gateway with Amazon DCV - Hub

```
Inputs:

- SSM Parameter Store
  - /WorkstationManagement/Leostream/DNSName
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/Leostream/RDS/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/ImageBuilder/InstanceProfile/Name
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /WorkstationManagement/Leostream/BrokerLoadBalancerArn
  - /WorkstationManagement/Leostream/BrokerLoadBalancerSecurityGroupId
  - /WorkstationManagement/Leostream/BrokerHttpsListenerArn
  - /Identity/ActiveDirectoryDomainName
- Secrets Manager
  - /Identity/StudioAdminActiveDirectoryLoginCredentials
  - /WorkstationManagement/Leostream/Console/AdminUserCredentials

Outputs:

- SSM Parameter Store
  - /PixelStreaming/AmazonDcv/PublicDomain
  - /PixelStreaming/AmazonDcv/LeostreamGateway/AMI-Id
```

Leostream Gateway with Amazon DCV - Spoke

```
Inputs:

- SSM Parameter Store
  - /Core/HubRegion
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /WorkstationManagement/Leostream/DNSName
  - /WorkstationManagement/Leostream/API/ServiceUserCredentials/SecretArn
  - /WorkstationManagement/Leostream/RDS/ServiceUserCredentials/SecretArn
  - /PixelStreaming/AmazonDcv/PublicDomain (Remote)
  - /PixelStreaming/AmazonDcv/LeostreamGateway/AMI-Id (Remote)

Outputs:

- SSM Parameter Store
  - /PixelStreaming/AmazonDcv/PublicDomain
```

FSx for Windows File Server

```
Inputs:

- SSM Parameter Store
  - /Network/VpcId
  - /Network/VpcCidr
  - /Network/PrivateSubnet1/AZ
  - /Network/PrivateSubnet1/SubnetID
  - /Network/PrivateSubnet1/RouteTableID
  - /Network/PrivateSubnet2/AZ
  - /Network/PrivateSubnet2/SubnetID
  - /Network/PrivateSubnet2/RouteTableID
  - /Identity/ActiveDirectoryServerIP1
  - /Identity/ActiveDirectoryServerIP2
  - /Identity/ActiveDirectoryDomainName
- Secrets Manager
  - /Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials

Outputs:

- SSM Parameter Store
  - /Storage/FSxWindowsFile/FSxWindowsname
  - /Storage/FSxWindowsFile/FSxResourceARN
```

Spoke Region Infrastructure

```
Inputs:

- SSM Parameter Store
  - /Core/MCSStack/Name (Remote)
  - /Core/AdminEmail (Remote)
  - /Core/Tag/Key (Remote)
  - /Core/Tag/Value/Linux (Remote)
  - /Core/Tag/Value/Windows (Remote)

Outputs:

- SSM Parameter Store
  - /Core/HubOrSpoke
  - /Core/HubRegion
  - /Core/Tag/Key
  - /Core/Tag/Value/Linux
  - /Core/Tag/Value/Windows
  - /Core/MCSStack/Name
  - /Core/MyApplication/Tag
  - /Core/AdminEmail
```
