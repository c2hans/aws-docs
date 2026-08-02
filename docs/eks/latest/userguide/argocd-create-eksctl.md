---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/argocd-create-eksctl.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability using eksctl
<a name="argocd-create-eksctl"></a>

Create an Argo CD capability on your Amazon EKS cluster using eksctl.

**Note**
The following steps require eksctl version `0.215.0` or later. To check your version, run `eksctl version`.

## Step 1: Create an IAM Capability Role
<a name="_step_1_create_an_iam_capability_role"></a>

Create a trust policy file:

```
cat > argocd-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "capabilities.eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
EOF
```

Create the IAM role:

```
aws iam create-role \
  --role-name ArgoCDCapabilityRole \
  --assume-role-policy-document file://argocd-trust-policy.json
```

**Note**
For this basic setup, no additional IAM policies are needed. If you plan to use Secrets Manager for repository credentials or CodeConnections, you’ll need to add permissions to the role. For IAM policy examples and configuration guidance, see [Manage application secrets with AWS Secrets Manager](integration-secrets-manager.md) and [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md).

## Step 2: Get your AWS Identity Center configuration
<a name="step_2_get_your_shared_aws_identity_center_configuration"></a>

Get your Identity Center instance ARN and user ID for RBAC configuration:

```
# Get your Identity Center instance ARN
aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text

# Get a user ID for admin access (replace 'your-username' with your Identity Center username)
aws identitystore list-users \
  --identity-store-id $(aws sso-admin list-instances --query 'Instances[0].IdentityStoreId' --output text) \
  --query 'Users[?UserName==`your-username`].UserId' --output text
```

Note these values - you’ll need them in the next step.

## Step 3: Create an eksctl configuration file
<a name="_step_3_create_an_eksctl_configuration_file"></a>

Create a file named `argocd-capability.yaml` with the following content. Replace the placeholder values with your cluster’s name, cluster’s region, IAM role ARN, Identity Center instance ARN, Identity Center region, and user ID:

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: {{my-cluster}}
  region: {{cluster-region-code}}

capabilities:
  - name: my-argocd
    type: ARGOCD
    roleArn: {{arn:aws:iam::111122223333:role/ArgoCDCapabilityRole}}
    deletePropagationPolicy: RETAIN
    configuration:
      argocd:
        awsIdc:
          idcInstanceArn: {{arn:aws:sso:::instance/ssoins-123abc}}
          idcRegion: {{idc-region-code}}
        rbacRoleMappings:
          - role: ADMIN
            identities:
              - id: {{38414300-1041-708a-01af-5422d6091e34}}
                type: SSO_USER
```

**Note**
You can add multiple users or groups to the RBAC mappings. For groups, use `type: SSO_GROUP` and provide the group ID. Available roles are `ADMIN`, `EDITOR`, and `VIEWER`.

## Step 4: Create the Argo CD capability
<a name="_step_4_create_the_argo_cd_capability"></a>

Apply the configuration file:

```
eksctl create capability -f argocd-capability.yaml
```

The command returns immediately, but the capability takes some time to become active.

## Step 5: Verify the capability is active
<a name="_step_5_verify_the_capability_is_active"></a>

Check the capability status. Replace {{region-code}} with the AWS Region that your cluster is in and replace {{my-cluster}} with the name of your cluster.

```
eksctl get capability \
  --region {{region-code}} \
  --cluster {{my-cluster}} \
  --name my-argocd
```

The capability is ready when the status shows `ACTIVE`.

## Step 6: Verify custom resources are available
<a name="_step_6_verify_custom_resources_are_available"></a>

After the capability is active, verify that Argo CD custom resources are available in your cluster:

```
kubectl api-resources | grep argoproj.io
```

You should see `Application` and `ApplicationSet` resource types listed.

## Next steps
<a name="_next_steps"></a>
+  [Working with Argo CD](working-with-argocd.md) - Learn how to create and manage Argo CD Applications
+  [Argo CD considerations](argocd-considerations.md) - Configure SSO and multi-cluster access
+  [Working with capability resources](working-with-capabilities.md) - Manage your Argo CD capability resource
