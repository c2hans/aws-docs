---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/anatomy.html
---

# Golden image anatomy
<a name="anatomy"></a>

AWS IoT Greengrass core devices that are manufactured at scale are generally embedded Linux devices that have a Linux distribution that's constructed by using tools such as [Yocto](https://www.yoctoproject.org/). Typically, the Greengrass edge runtime is baked into the distribution, as demonstrated by the [Meta AWS](https://github.com/aws4embeddedlinux/meta-aws) project.

Such devices often have their file system organized into multiple partitions. This guide uses *golden image* as a catch-all term. Your device might have several golden images, to flash the various partitions.

Your golden image might encompass the entirety of the device's file system or just part of it. This guide focuses on the parts of the file system you need to consider for AWS IoT Greengrass, without prescribing how to assemble your images more broadly.

## Greengrass directory tree
<a name="greengrass-directory"></a>

To understand the golden image methods discussed in this guide, review the structure of the Greengrass directory tree shown in the following table.

|
|
| **Directory** | **Description** |
| --- |--- |
| `alts` | Launch parameters and symbolic links to the Greengrass nucleus version that is currently active. |
| `bin` | Binaries, if any are installed (for example, the [Greengrass CLI](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-cli-component.html) binary if that component is installed). This directory is often empty. |
| `cli_ipc_info` | Scratchpad for Greengrass CLI interprocess communication (IPC). This directory is empty if you haven't installed the Greengrass CLI. |
| `config` | All Greengrass configuration, including component configuration. |
| `deployments` | Data for managing the state of deployments and rollbacks. |
| `logs` | Log files for the nucleus and other components. |
| `packages` | Artifacts and recipes for all components. |
| `plugins` | Storage for components of type `aws.greengrass.plugin` that you manually installed. Otherwise, this directory holds no data. |
| `telemetry` | Scratchpad used by Greengrass to aggregate telemetry data ready for publishing. |
| `work` | Scratchpad for components. |

The `logs`, `telemetry`, and `work` directories contain only ephemeral data. They don't need be included in a golden image, so omit them if you want to minimize the size of the image.

The Greengrass CLI isn't usually installed on production devices, so the `bin` and `cli_ipc_info` directories are often empty and don't typically need to be included in a golden image.

The `plugins` directory includes data only if you manually installed a plugin (such as the [fleet provisioning plugin](https://docs.aws.amazon.com/greengrass/v2/developerguide/fleet-provisioning.html#download-fleet-provisioning-plugin) or a custom provisioning plugin) when you installed Greengrass.

The data in the `deployments` directory is used only when a deployment is in progress and therefore isn't needed in a golden image.

Consequently the `alts`, `config` and `packages` directories are of the greatest interest. Sometimes these are the only Greengrass directories you need to include in a golden image, if you want to minimize the image size.

## Contents of the packages directory
<a name="packages-directory"></a>

The packages directory has three subdirectories, as shown in the following table.

|
|
| **Sub-directory** | **Description** |
| --- |--- |
| `artifacts` | The zipped component artifacts that Greengrass downloads during deployments. |
| `artifacts-unarchived` | For artifacts that are `.zip` archives, this directory contains the same artifacts, but they are unzipped so that components can use the artifact contents. |
| `recipes` | The component recipe files. |

### artifacts
<a name="artifacts.1cd98861-98c5-5536-a55a-f3ddc193145f"></a>

The following example tree listing of `packages/artifacts` shows how artifacts are stored.

```
user@machine:~$ sudo tree /greengrass/v2/packages/artifacts
/greengrass/v2/packages/artifacts
├── aws.greengrass.DockerApplicationManager
├── aws.greengrass.LogManager
│   └── 2.3.7
│       └── aws.greengrass.LogManager.jar
├── aws.greengrass.Nucleus
│   └── 2.12.6
│       └── aws.greengrass.nucleus.zip
├── aws.greengrass.SecretManager
│   └── 2.1.8
│       └── aws.greengrass.SecretManager.jar
├── aws.greengrass.SecureTunneling
│   └── 1.0.19
│       └── GreengrassV2SecureTunnelingComponent-1.0-all.jar
├── aws.greengrass.labs.CertificateRotator
│   └── 1.1.0
│       └── certificate-rotator.zip
├── aws.greengrass.labs.HomeAssistant
│   └── 1.0.0
│       └── home-assistant.zip
└── aws.greengrass.telemetry.NucleusEmitter
    └── 1.0.8
        └── aws.greengrass.telemetry.NucleusEmitter.jar

15 directories, 7 files
```

### artifacts-unarchived
<a name="artifacts-unarchived.5b94e510-bb62-5e5e-b849-33daf21eb56a"></a>

The following example tree listing of `packages/artifacts-unarchived` shows artifacts that are extracted from `.zip` files.

```
user@machine:~$ sudo tree /greengrass/v2/packages/artifacts-unarchived
/greengrass/v2/packages/artifacts-unarchived
├── aws.greengrass.Nucleus
│   └── 2.12.6
│       └── aws.greengrass.nucleus
│           ├── LICENSE
│           ├── NOTICE
│           ├── README.md
│           ├── THIRD-PARTY-LICENSES
│           ├── bin
│           │   ├── greengrass.exe
│           │   ├── greengrass.service
│           │   ├── greengrass.service.procd.template
│           │   ├── greengrass.service.template
│           │   ├── greengrass.xml.template
│           │   ├── loader
│           │   └── loader.cmd
│           ├── conf
│           │   └── recipe.yaml
│           └── lib
│               └── Greengrass.jar
├── aws.greengrass.SecureTunneling
│   └── 1.0.19
├── aws.greengrass.labs.CertificateRotator
│   └── 1.1.0
│       └── certificate-rotator
│           ├── __pycache__
│           │   ├── config.cpython-310.pyc
│           │   ├── config.cpython-311.pyc
│           │   ├── effective_config.cpython-310.pyc
│           │   ├── effective_config.cpython-311.pyc
│           │   ├── main.cpython-311.pyc
│           │   ├── pki.cpython-310.pyc
│           │   ├── pki.cpython-311.pyc
│           │   ├── pki_file.cpython-310.pyc
│           │   ├── pki_file.cpython-311.pyc
│           │   ├── pki_hsm.cpython-310.pyc
│           │   ├── pki_hsm.cpython-311.pyc
│           │   ├── pubsub.cpython-310.pyc
│           │   ├── pubsub.cpython-311.pyc
│           │   ├── state.cpython-310.pyc
│           │   ├── state.cpython-311.pyc
│           │   ├── state_committing_certificate.cpython-310.pyc
│           │   ├── state_committing_certificate.cpython-311.pyc
│           │   ├── state_creating_certificate.cpython-310.pyc
│           │   ├── state_creating_certificate.cpython-311.pyc
│           │   ├── state_getting_job.cpython-310.pyc
│           │   ├── state_getting_job.cpython-311.pyc
│           │   ├── state_idle.cpython-310.pyc
│           │   ├── state_idle.cpython-311.pyc
│           │   ├── state_machine.cpython-310.pyc
│           │   ├── state_machine.cpython-311.pyc
│           │   ├── state_updating_job.cpython-310.pyc
│           │   ├── state_updating_job.cpython-311.pyc
│           │   ├── topic_base.cpython-310.pyc
│           │   └── topic_base.cpython-311.pyc
│           ├── config.py
│           ├── effective_config.py
│           ├── main.py
│           ├── pki.py
│           ├── pki_file.py
│           ├── pki_hsm.py
│           ├── pubsub.py
│           ├── requirements.txt
│           ├── scripts
│           │   └── run.cmd
│           ├── state.py
│           ├── state_committing_certificate.py
│           ├── state_creating_certificate.py
│           ├── state_getting_job.py
│           ├── state_idle.py
│           ├── state_machine.py
│           ├── state_updating_job.py
│           └── topic_base.py
└── aws.greengrass.labs.HomeAssistant
    └── 1.0.0
        └── home-assistant
            ├── config
            │   ├── automations.yaml
            │   ├── configuration.yaml
            │   ├── groups.yaml
            │   ├── scenes.yaml
            │   └── scripts.yaml
            ├── docker-compose.yml
            ├── install.py
            └── secret.py

17 directories, 67 files
```

Note that the `alts` directory links to the Nucleus `.jar` file in `packages/artifacts-unarchived`. For example:

```
user@machine:~$ sudo ls -l /greengrass/v2/alts/init
total 8
lrwxrwxrwx 1 root root 97 Jun 27 08:12 distro -> /greengrass/v2/packages/artifacts-unarchived/aws.greengrass.Nucleus/2.12.6/aws.greengrass.nucleus
-rw-r--r-- 1 root root 16 Jun 27 07:07 launch.params
```

Therefore, `packages/artifacts-unarchived` must be included in your golden image.

### recipes
<a name="recipes.0f0c7dd6-563e-5cfe-8604-a255e1bb2ff8"></a>

The following example tree listing of `packages/recipes` shows how recipes are stored. As the listing indicates, recipes are stored with digests to help Greengrass determine whether it already has the correct files when it receives a deployment. This highly specific format makes it difficult to compose a golden image. Consequently, taking a snapshot of a golden device is the recommended method for creating a golden image.

```
user@machine:~$ sudo tree /greengrass/v2/packages/recipes
/greengrass/v2/packages/recipes
├── 0ya1warrMfzlq5PUTvOgfHOununru_xCLUFACECM_R0@2.3.7.metadata.json
├── 0ya1warrMfzlq5PUTvOgfHOununru_xCLUFACECM_R0@2.3.7.recipe.yaml
├── 89r1-ak7xPauDt4O7EG03sSXVUO8ysdHTk-YdF0NAAc@2.12.6.metadata.json
├── 89r1-ak7xPauDt4O7EG03sSXVUO8ysdHTk-YdF0NAAc@2.12.6.recipe.yaml
├── VAZ-Grqe5g43yO7UtasQOR5jcQGILgPeRZQhVikLd9o@1.0.0.metadata.json
├── VAZ-Grqe5g43yO7UtasQOR5jcQGILgPeRZQhVikLd9o@1.0.0.recipe.yaml
├── ViMYPYs99-AzSt1gL2L2YD5P7sIN-yEhy23wWJK_JN8@1.0.8.metadata.json
├── ViMYPYs99-AzSt1gL2L2YD5P7sIN-yEhy23wWJK_JN8@1.0.8.recipe.yaml
├── _1hT2A6X0ZYtB_CfI_ZUOEMDV96DfQVkSmZh2bbGYXg@1.0.19.metadata.json
├── _1hT2A6X0ZYtB_CfI_ZUOEMDV96DfQVkSmZh2bbGYXg@1.0.19.recipe.yaml
├── gQWwM7MSL2kOsBADU9bOQJ1QqO8ZI3hqpbKT5Bv4Ijk@1.1.0.metadata.json
├── gQWwM7MSL2kOsBADU9bOQJ1QqO8ZI3hqpbKT5Bv4Ijk@1.1.0.recipe.yaml
├── j_j5Seyy01FOcIh95nBFy4HYf8P1kT-jW_nmV18ldbk@2.1.8.metadata.json
└── j_j5Seyy01FOcIh95nBFy4HYf8P1kT-jW_nmV18ldbk@2.1.8.recipe.yaml

0 directories, 14 files
```

## System service
<a name="systemd"></a>

If Greengrass is installed as a system service, as it commonly is for embedded Linux devices, the golden image must also include the directories that contain the `systemd` startup scripts.

## Docker images
<a name="docker"></a>

If your device uses AWS IoT Greengrass components that feature Docker images as artifacts, these artifacts sit outside the Greengrass directory tree. Therefore, you need to include the golden device's Docker image registry in your golden image. This registry is typically stored in `/var/lib/docker`.

Alternatively, you can use Docker commands to make a copy of the Docker images that are stored on your golden device, and then load those Docker images onto each device on your manufacturing line. In general, this method is slower and becomes less scalable as the number of Docker images increases.

## Secrets
<a name="secrets"></a>

If your devices use the [secret manager component](https://docs.aws.amazon.com/greengrass/v2/developerguide/secret-manager-component.html) to synchronize secrets from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), these secrets are stored in the `config/config.tlog` file in the Greengrass directory tree of your golden device. For example:

```
{"TS":1718878001465,
 "TP":["services","aws.greengrass.SecretManager","runtime","secretResponse"],
 "W":"changed",
 "V":"{\"secrets\":[
          {
           \"arn\":\"arn:aws:secretsmanager:us-east-1:111122223333:secret:greengrass-home-assistant-KIzJfZ\",
           \"name\":\"greengrass-home-assistant\",
           \"versionId\":\"8e481177-9250-4458-9f1f-3690d28e4ae9\",
           \"encryptedSecretString\":\"AgV4j+We ... A7QjdE1w==\",
           \"versionStages\":[\"AWSCURRENT\"],
           \"createdDate\":1660648425915
          }
       ]
    }
"}
```

These secrets are also stored in the corresponding `config/effectiveConfig.yaml` file:

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

Even if you include the `config` directory in your golden image, it's important to remember that the Greengrass [secret manager component encrypts the secret with the golden device's private key](https://docs.aws.amazon.com/greengrass/v2/developerguide/secret-manager-component.html). Because each device has a unique private key, keys that were encrypted by your golden device can't be decrypted by your production devices.

For this reason, we recommend that you remove encrypted secrets from the golden image to prevent your production devices from incorrectly decrypting golden device secrets. Your application components should function adequately, or at least fail gracefully, when secrets aren't present on disk, before a device has its first communication with the cloud.

### When secrets are a hard requirement
<a name="when-secrets-are-a-hard-requirement.a43cb13e-9888-51eb-966b-de0c6031fd0d"></a>

If your organization requires your production devices to be populated with secrets during manufacture, your production line needs a script or program that replicates the behavior of the secret manager component, to populate secrets on each production device. We don't recommend this approach because of its complexity and the possibility that your secrets might briefly be held in cleartext on your production programming station.
