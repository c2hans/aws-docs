---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/interaction-steps.html
---

# Interaction steps
<a name="interaction-steps"></a>

 This section details how to configure AWS Network Firewall to interoperate with this solution, create example objects, and a rule that references these objects.
+  Create an ANFW rule group to hold the resultant rules created by the solution.
+  Create a rule bundle within the solution, to hold the dynamic rules defined by the security operator.
+  Create objects to be referenced within the solution rules.
+  Create rules within the rule bundle, which contain references to the objects created earlier.
+  The solution populates the ANFW rule group with the defined rules as objects are resolved through querying the AWS Config aggregator.

## Identify a host machine with which to interact with the solution
<a name="identify-a-host-machine-with-which-to-interact-with-the-solution"></a>

 If you are interacting with the solution from a machine within AWS, rather than a local desktop, complete the following steps.

**Note**
 The following section is required if configuration `apiGatewayType` is set to `private`. You must complete the following steps while logged into EC2 via Session Manager.

1.  Sign in to the [AWS Systems Manager Session Manager](https://console.aws.amazon.com/systems-manager/home) console.

1.  Choose **Start Session**.

1.  Select the target instance. For details, refer to [Create an EC2 instance](operation-and-customization.md#create-an-ec2-instance).

1.  Choose **Start Session**.

 If configuration `apiGatewayType` is set to `edge`, complete the following step on your local machine to interact with the solution’s Edge-optimized API endpoint.

 If configuration `apiGatewayType` is set to `private` (default), complete the following steps from the EC2 Session Manager’s connection opened in the previous step to interact with the solution’s private API endpoint.

## Install the prerequisite tools
<a name="install-the-prerequisite-tools"></a>

1.  Install JQ. Refer to [Install JQ](operation-and-customization.md#install-jq) for more information.

1.  Install awscurl. Refer to [Install awscurl](operation-and-customization.md#install-aws-curl) for more information.

1.  On Mac OS X, install GNU getopt. Refer to [Install GNU getopt](operation-and-customization.md#install-gnu-getopt) for more information.

## Create a Network Firewall rule group
<a name="create-a-network-firewall-rule-group"></a>

1.  Sign in to the AWS Management Console.

1.  Select **VPC,** then select **Network Firewall Rule Groups** in the left navigation menu.

1.  On the Network Firewall rule groups page, choose **Create Network Firewall rule group**.

1.  Select **Stateful rule group.**

1.  Make sure the Stateful rule group name is aligned with the pattern in configuration section’s `networkFirewallRuleGroupNamePattern`. If the pattern is `default-ANFW-CONFIG-*`, then the rule group name should be `default-ANFW-CONFIG-rule1`, so that this solution can request the resource from ANFW correctly.

1.  Fill **Capacity** value, we recommend at least 15,000 for this solution.

1.  Select **IP***,* then add a default rule.

1.  Choose **Create stateful rule group.**

    Record the name of the stateful rule group you created. You will use it in [Use CLI tool to create solution rule bundle entity](#use-cli-tool-to-create-solution-rule-bundle-entity).

 The following section describes the process for creating a new object and a rule group, then adding a rule in the new rule group to reference the object.

## Use CLI tool to create solution rule bundle entity
<a name="use-cli-tool-to-create-solution-rule-bundle-entity"></a>

1.  Ensure you are using GNU getopt command line tool. This is the default on Linux.  If you are using the CLI on Mac OS X, refer to [Install GNU Getopt](operation-and-customization.md#install-gnu-getopt) for instructions about installing GNU getopt. Ensure you have set the environment variable `GNU_GETOPT_PATH` if GNU getopt is not in your path already.

   ```
   export GNU_GETOPT_PATH=/usr/local/opt/gnu-getopt/bin/getopt
   ```

1.  Run the following command to set account this solution is installed:

   ```
   export ACCOUNT_NUMBER=1234567
   ```

1.  Run the following command to set the API\_ENDPOINT that the solution created during installation:

   ```
   export API_ENDPOINT=[https://yourAPIendpoint.execute-api.ap-southeast-2.amazonaws.com/prod](https://2zzlmuebx5.execute-api.ap-southeast-2.amazonaws.com/prod)
   ```

    The API\_ENDPOINT can be found in the CloudFormation console as below

1.  Run the following command to set ROLEARN to allow the user to interact with API gateway of this solution:

   ```
   export ROLEARN=$(aws iam get-role --role-name "ObjectExtensionSecOpsAdminRole"-{{<region>}} | jq -r .Role.Arn)
   ```

1.  Assume to SecOps role using ROLEARN from above.

   ```
   export ASSUMEROLE=$(aws sts assume-role --role-arn $ROLEARN --role-session-name DeviceClient --duration-second 3600)
   export AWS_ACCESS_KEY_ID=$(echo $ASSUMEROLE | jq -r .Credentials.AccessKeyId)
   export AWS_SECRET_ACCESS_KEY=$(echo $ASSUMEROLE | jq -r .Credentials.SecretAccessKey)
   export AWS_SESSION_TOKEN=$(echo $ASSUMEROLE | jq -r .Credentials.SessionToken)
   ```

1.  Run the following command to set AWS\_REGION to ensure your credentials are used in the same region that the API is hosted:

   ```
   export AWS_REGION=<solution aws region>
   ```

1.  Run the following command to set RULE\_GROUP\_NAME to the rule group you created earlier:

   ```
   export RULE_GROUP_NAME=<name of stateful rule group from previous step>

   Example:
   export RULE_GROUP_NAME=anfwconfig-testrulegroup-demo-001

   Run the following commands:

   cd scripts

   ./aoe.sh create-rule-bundle --rule-bundle-id example-rule-bundle-1 --rule-bundle-description "Example Solution Rule Bundle" --rule-group-arn arn:aws:network-firewall:ap-southeast-2:${ACCOUNT_NUMBER}:stateful-rulegroup/${RULE_GROUP_NAME} --rule-bundle-owner-group "${ROLEARN}"
   ```

    Expected output:

   ```
   {
   "ruleBundleId": "example-rule-bundle-1"
   }
   ```

## Create an object to represent the underlying cloud resource
<a name="create-an-object-to-represent-the-underlying-cloud-resource"></a>

1.  Create an EC2 instance, find its `instance id`, and set the environment EC2\_ARN.

   ```
   export EC2_ARN="arn:aws:ec2:ap-southeast-2:${ACCOUNT_NUMBER}:instance/<instance id>"
   ```

1.  Create an object reference to this Arn with the following command:

   ```
   ./aoe.sh create-object --object-id "MyExampleObject" --object-type "Arn" --object-value ${EC2_ARN}
   ```

    Expected output:

   ```
   {
     "object": {
       "id": "MyExampleObject",
       "type": "Arn",
       "value": "arn:aws:ec2:ap-southeast-2:111111111:instance/i-0564e8a206c6fb237",
       "createdBy": "arn:aws:sts::111111111:assumed-role/ObjectExtensionSecOpsAdminRole/DeviceClient",
       "lastUpdated": "2021-10-15T00:32:38.723Z"
     }
   }
   ```

1.  Create one additional fixed object with the following command. This is an object to represent IP 172.16.1.20 and port `1234`:

   ```
   ./aoe.sh create-object --object-id "OnPremServer" --object-type "Address" --object-value 172.16.1.20
   ```

    Expected output:

   ```
   {
       "object": {
           "id": "OnPremServer",
           "type": "Address",
           "value": "172.16.1.20",
           "createdBy": "arn:aws:sts::<ACCOUNT_ID>:assumed-role/ObjectExtensionSecOpsAdminRole/DeviceClient",
           "lastUpdated": "2021-10-07T01:43:29.854Z"
       }
   }
   ```

## Create a rule in the rule bundle
<a name="create-a-rule-in-the-rule-bundle"></a>

1.  Use the following command to create a new rule, which references both objects created in the previous step.

   ```
   ./aoe.sh create-rule --rule-bundle-id example-rule-bundle-1 --rule-protocol tcp --rule-action pass --rule-source
   OnPremServer --source-port-type SinglePort --source-port-value 1234 --rule-destination MyExampleObject --destination-port-type Any
   ```

    Expected output:

   ```
   {
     "rule": {
       "protocol": "tcp",
       "action": "pass",
       "source": "OnPremServer",
       "sourcePort": {
         "type": "SinglePort",
         "value": "1234"
       },
       "destination": "MyExampleObject",
       "destinationPort": {
         "type": "Any"
       },
       "status": "PENDING",
       "ruleBundleId": "example-rule-bundle-1",
       "lastUpdated": "2021-10-15T00:37:07.576Z",
       "id": "94bbbb56-fd3d-4f80-a74f-749b4d907fb9",
       "version": 0
     }
   }
   ```

1.  At this point, the solution will process the rule in the next cycle and automatically configure ANFW with a rule that reflects the resolved addresses of both objects. Refer to the ANFW console.
