---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/procedure.html
---

# Golden image procedure
<a name="procedure"></a>

The following sections describe the procedure for creating a golden image and writing that image to each device on the production line.

## Create your golden device
<a name="create"></a>

**Step 1: Install and provision Greengrass.**

[Install the Greengrass edge runtime](https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-core-v2.html) on your golden device as you typically would, and provision it by using your preferred [provisioning method](https://docs.aws.amazon.com/iot/latest/developerguide/iot-provision.html).

**Step 2: Deploy your components.**

From the cloud, deploy your application components and configuration to your golden device, as you typically would.

## Read the golden image from your golden device
<a name="read"></a>

You can now snapshot your golden device to create a golden image.

**Step 1: Shut down Greengrass**.

Shut down the Greengrass service on your golden device. For example:

```
sudo systemctl stop greengrass.service
```

**Step 2: Snapshot the Greengrass file tree**.

Depending on your preferred golden method, take a full or partial snapshot of the Greengrass file tree, and include it in your golden image.

**Step 3: Copy your Docker images**.

If your components use Docker images as artifacts, take a snapshot of the Docker image registry and include it in your golden image.

Alternatively, you can use `docker save` to create an archive of each Docker image, and copy these from the golden device. For example:

```
user@machine:~/environment $ docker images
REPOSITORY                     TAG       IMAGE ID       CREATED      SIZE
homeassistant/home-assistant   2024.6    2b4c9de733f1   9 days ago   1.6GB
user@machine:~/environment $ docker save homeassistant/home-assistant | gzip > home-assistant.tar.gz
```

In general, this approach is slower than adding the Docker image registry to your golden image.

## Write the golden image to your production devices
<a name="write"></a>

You now need to write the golden image to each of your production devices that come through your manufacturing line. The following steps would typically be automated by using scripting.

**Step 1: Write the image**.

Write your golden image to the production device. Make sure that it includes the full or partial snapshot of the Greengrass directory tree and the Docker image registry, as applicable.

**Step 2: Load Docker images**.

If you elected to use `docker save` to copy Docker image artifacts from your golden device, use `docker load` to load these images onto your production device. For example:

```
user@machine:~/environment $ docker load < home-assistant.tar.gz
user@machine:~/environment $ docker images
REPOSITORY                     TAG       IMAGE ID       CREATED      SIZE
homeassistant/home-assistant   2024.6    2b4c9de733f1   9 days ago   1.6GB
```

In general, this approach is slower than adding the Docker image registry to your golden image.

**Step 3: Add credentials**.

If your device doesn't use [fleet provisioning](https://docs.aws.amazon.com/greengrass/v2/developerguide/fleet-provisioning.html), install the unique X.509 certificate and private key for the production device, replacing the golden device credentials. The exact method of achieving this depends on whether you use a [hardware security module (HSM)](https://docs.aws.amazon.com/greengrass/v2/developerguide/hardware-security.html) and your particular public key infrastructure (PKI).

## Configure your production devices
<a name="configure"></a>

### Full Greengrass snapshot method
<a name="full-greengrass-snapshot-method.cd98fc01-dc38-58f9-861c-c81d248cdc58"></a>

Follow these steps only if you're using the **full **Greengrass snapshot method.

**Step 1: Edit the configuration**.

Edit the `config/effectiveConfig.yaml` file . For example:

```
sudo nano /greengrass/v2/config/effectiveConfig.yaml
```

**Step 2: Set the thing name**.

The actions required to set the thing name of the new production device depend on whether you're using fleet provisioning. Make the correct modifications for your use case.

If you aren't using fleet provisioning, you can set the thing name of your production device by editing the `thingName` property to replace the golden device thing name with the production device thing name. For example:

```
system:
  certificateFilePath: "/greengrass/v2/thingCert.crt"
  privateKeyPath: "/greengrass/v2/privKey.key"
  rootCaPath: "/greengrass/v2/rootCA.pem"
  rootpath: "/greengrass/v2"
  thingName: "ProductionDeviceThingName1"
```

If you are using fleet provisioning, you must first erase part of the golden device configuration to ensure that the [fleet provisioning plugin](https://github.com/aws-greengrass/aws-greengrass-fleet-provisioning-by-claim) will run on the production device. You can do this by replacing the golden device thing name in the `thingName` property with an empty string. For example:

```
system:
  certificateFilePath: "/greengrass/v2/thingCert.crt"
  privateKeyPath: "/greengrass/v2/privKey.key"
  rootCaPath: "/greengrass/v2/rootCA.pem"
  rootpath: "/greengrass/v2"
  thingName: ""
```

Additionally, you must add the fleet provisioning plugin configuration to the `services` property, and pass the production device thing name as a property within the `templateParameters` property. The following example assumes that the [fleet provisioning template](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html#fleet-provision-template) has a parameter named `ThingName`, and therefore there's a `ThingName` property within the `templateParameters` of the plugin configuration:

```
system:
  certificateFilePath: "/greengrass/v2/thingCert.crt"
  privateKeyPath: "/greengrass/v2/privKey.key"
  rootCaPath: "/greengrass/v2/rootCA.pem"
  rootpath: "/greengrass/v2"
  thingName: ""
services:
  aws.greengrass.FleetProvisioningByClaim:
    configuration:
      rootPath: "/greengrass/v2"
      awsRegion: "us-east-1"
      iotDataEndpoint: "<prefix>-ats.iot.us-east-1.amazonaws.com"
      iotCredentialEndpoint: "<prefix>.credentials.iot.us-east-1.amazonaws.com"
      iotRoleAlias: "GreengrassCoreTokenExchangeRoleAlias"
      provisioningTemplate: "GreengrassFleetProvisioningTemplate"
      claimCertificatePath: "/greengrass/v2/claim-certs/claim.pem.crt"
      claimCertificatePrivateKeyPath: "/greengrass/v2/claim-certs/claim.private.pem.key"
      rootCaPath: "/greengrass/v2/rootCA.pem"
      templateParameters:
        ThingName: "ProductionDeviceThingName1"
```

Your use case might require some different fleet provisioning plugin configuration parameters than what's shown here. For more information, see [Configure the AWS IoT fleet provisioning plugin](https://docs.aws.amazon.com/greengrass/v2/developerguide/fleet-provisioning-configuration.html) in the AWS IoT Greengrass documentation.

**Step 3: Update interpolated thing names**.

If you have any components that use the `iot:thingName` [recipe variable](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html#recipe-variables) to [interpolate](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-interpolate-component-configuration) the thing name, you will likely have access control statements in which the golden device thing name has been interpolated. For example, in the case of the [Certificate Rotator community component](https://github.com/awslabs/aws-greengrass-labs-certificate-rotator):

```
services:
  aws.greengrass.labs.CertificateRotator:
    componentType: "GENERIC"
    configuration:
      accessControl:
        aws.greengrass.ipc.mqttproxy:
          aws.greengrass.labs.CertificateRotator:mqttproxy:1:
            operations:
            - "aws.greengrass#PublishToIoTCore"
            policyDescription: "Allows access to publish to relevant topics"
            resources:
            - "$aws/things/GoldenDeviceThingName/jobs/+/get"
            - "$aws/things/GoldenDeviceThingName/jobs/+/update"
            - "awslabs/things/GoldenDeviceThingName/certificate/create"
            - "awslabs/things/GoldenDeviceThingName/certificate/commit"
          aws.greengrass.labs.CertificateRotator:mqttproxy:2:
            operations:
            - "aws.greengrass#SubscribeToIoTCore"
            policyDescription: "Allows access to subscribe to relevant topics"
            resources:
            - "$aws/things/GoldenDeviceThingName/jobs/notify-next"
            - "$aws/things/GoldenDeviceThingName/jobs/+/get/accepted"
            - "$aws/things/GoldenDeviceThingName/jobs/+/get/rejected"
            - "$aws/things/GoldenDeviceThingName/jobs/+/update/accepted"
            - "$aws/things/GoldenDeviceThingName/jobs/+/update/rejected"
            - "awslabs/things/GoldenDeviceThingName/certificate/create/accepted"
            - "awslabs/things/GoldenDeviceThingName/certificate/create/rejected"
            - "awslabs/things/GoldenDeviceThingName/certificate/commit/accepted"
            - "awslabs/things/GoldenDeviceThingName/certificate/commit/rejected"
      keyAlgorithm: "RSA-2048"
      signingAlgorithm: "SHA256WITHRSA"
```

In all such cases, you must replace all instances of the golden device thing name with your production device thing name.

**Step 4: Remove golden device secrets**.

Examine `effectiveConfig.yaml` for any encrypted secrets that were stored by your golden device. These will be stored within the secret manager component configuration. For example:

```
  aws.greengrass.SecretManager:
    componentType: "PLUGIN"
    configuration:
      cloudSecrets:
      - arn: "arn:aws:secretsmanager:us-east-1:111122223333:secret:greengrass-home-assistant-KIzJfZ"
    dependencies:
    - "aws.greengrass.Nucleus:SOFT"
    lifecycle: {}
    runtime:
      secretResponse: "{\"secrets\":[{\"arn\":\"arn:aws:secretsmanager:us-east-1:111122223333:secret:greengrass-home-assistant-KIzJfZ\"\
        ,\"name\":\"greengrass-home-assistant\",\"versionId\":\"8e481177-9250-4458-9f1f-3690d28e4ae9\"\
        ,\"encryptedSecretString\":\"AgV4Rpc9 ... MYeVALYQ==\"\
        ,\"versionStages\":[\"AWSCURRENT\"],\"createdDate\":1660648425915}]}"
    version: "2.1.8"
```

You should delete this secret to ensure that your production device will not attempt to decrypt a secret that was encrypted by the golden device. Delete the `secretResponse` property. For example:

```
  aws.greengrass.SecretManager:
    componentType: "PLUGIN"
    configuration:
      cloudSecrets:
      - arn: "arn:aws:secretsmanager:us-east-1:111122223333:secret:greengrass-home-assistant-KIzJfZ"
    dependencies:
    - "aws.greengrass.Nucleus:SOFT"
    lifecycle: {}
    runtime:
    version: "2.1.8"
```

**Step 5: Apply the altered configuration**.

Apply the altered configuration, to update `config/config.tlog`. For example:

```
sudo java -Droot="/greengrass/v2" \
  -jar /greengrass/v2/alts/current/distro/lib/Greengrass.jar \
  --start false \
  --init-config /greengrass/v2/config/effectiveConfig.yaml
```

### Partial Greengrass snapshot method
<a name="partial-greengrass-snapshot-method.216c1c3f-56c4-5c40-bd1b-5b6b8ae04ae7"></a>

Configuration of your production devices is trivial if you use the partial Greengrass snapshot method. The procedure is identical to the normal bootstrap partial configuration procedure when you [install Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-core-v2.html), except that the initial configuration is passed to the Greengrass runtime that's already installed.

Follow these steps only if you're using the **partial** Greengrass snapshot method.

**Step 1: Create the configuration**.

The required partial configuration depends on whether you're using fleet provisioning. Be sure to make the correct modifications for your use case.

If you aren't using fleet provisioning, you can create a partial configuration file that doesn't include any configuration for the fleet provisioning plugin. Set the `thingName` property to your production device thing name. For example:

```
system:
  certificateFilePath: "/greengrass/v2/device.pem.crt"
  privateKeyPath: "/greengrass/v2/private.pem.key"
  rootCaPath: "/greengrass/v2/AmazonRootCA1.pem"
  rootpath: "/greengrass/v2"
  thingName: "ProductionDeviceThingName1"
services:
  aws.greengrass.Nucleus:
    componentType: "NUCLEUS"
    version: "2.12.6"
    configuration:
      awsRegion: "us-east-1"
      iotRoleAlias: "GreengrassCoreTokenExchangeRoleAlias"
      iotDataEndpoint: "<prefix>-ats.iot.us-east-1.amazonaws.com"
      iotCredEndpoint: "<prefix>.credentials.iot.us-east-1.amazonaws.com"
```

If you are using fleet provisioning, the partial configuration should include configuration for the [fleet provisioning plugin](https://github.com/aws-greengrass/aws-greengrass-fleet-provisioning-by-claim). This configuration should pass the production device thing name as a property within the `templateParameters` property. The following example assumes that the [fleet provisioning template](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html#fleet-provision-template) has a parameter named `ThingName`, and therefore there's a `ThingName` property within the `templateParameters` of the plugin configuration:

```
services:
  aws.greengrass.Nucleus:
    version: "2.12.6"
  aws.greengrass.FleetProvisioningByClaim:
    configuration:
      rootPath: "/greengrass/v2"
      awsRegion: "us-east-1"
      iotDataEndpoint: "<prefix>-ats.iot.us-east-1.amazonaws.com"
      iotCredentialEndpoint: "<prefix>.credentials.iot.us-east-1.amazonaws.com"
      iotRoleAlias: "GreengrassCoreTokenExchangeRoleAlias"
      provisioningTemplate: "GreengrassFleetProvisioningTemplate"
      claimCertificatePath: "/greengrass/v2/claim-certs/claim.pem.crt"
      claimCertificatePrivateKeyPath: "/greengrass/v2/claim-certs/claim.private.pem.key"
      rootCaPath: "/greengrass/v2/AmazonRootCA1.pem"
      templateParameters:
        ThingName: "ProductionDeviceThingName1"
```

Your use case might require different fleet provisioning plugin configuration parameters from what's shown here. For more information, see [Configure the AWS IoT fleet provisioning plugin](https://docs.aws.amazon.com/greengrass/v2/developerguide/fleet-provisioning-configuration.html) in the AWS IoT Greengrass documentation.

**Step 2: Apply the configuration.**

Apply the configuration to create `config/config.tlog`. For example:

```
sudo java -Droot="/greengrass/v2" \
  -jar /greengrass/v2/alts/current/distro/lib/Greengrass.jar \
  --start false \
  --init-config config.yaml
```
