---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html
---

# Identify duplicate container images automatically when migrating to an Amazon ECR repository
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository"></a>

*Rishabh Yadav and Rishi Singla, Amazon Web Services*

## Summary
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-summary"></a>

The pattern provides an automated solution to identify whether images that are stored in different container repositories are duplicates. This check is useful when you plan to migrate images from other container repositories to Amazon Elastic Container Registry (Amazon ECR).

For foundational information, the pattern also describes the components of a container image, such as the image digest, manifest, and tags. When you plan a migration to Amazon ECR, you might decide to synchronize your container images across container registries by comparing the digests of the images. Before you migrate your container images, you need to check whether these images already exist in the Amazon ECR repository to prevent duplication. However, it can be difficult to detect duplication by comparing image digests, and this might lead to issues in the initial migration phase.  This pattern compares the digests of two similar images that are stored in different container registries and explains why the digests vary, to help you compare images accurately.

## Prerequisites and limitations
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-prereqs"></a>
+ An active AWS account
+ Access to the [Amazon ECR public registry](https://gallery.ecr.aws/)
+ Familiarity with the following AWS services:
  + [AWS CodeCommit](https://aws.amazon.com/codecommit/)
  + [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
  + [AWS CodeBuild](https://aws.amazon.com/codebuild/)
  + [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
  + [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
+ Configured CodeCommit credentials (see [instructions](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html))

## Architecture
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-architecture"></a>

**Container image components**

The following diagram illustrates some of the components of a container image. These components are described after the diagram.

![Manifest,configuration, file system layers, and digests.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7db5020c-6f5b-4e91-b91a-5b8ae844be1b/images/71b99c67-a934-4f94-8af8-2a8431fb91f5.png)

**Terms and definitions**

The following terms are defined in the [Open Container Initiative (OCI) Image Specification](https://github.com/opencontainers/image-spec/blob/main/spec.md).
+ **Registry:** A service for image storage and management.
+ **Client:** A tool that communicates with registries and works with local images.
+ **Push:** The process for uploading images to a registry.
+ **Pull:** The process for downloading images from a registry.
+ **Blob:** The binary form of content that is stored by a registry and can be addressed by a digest.
+ **Index:** A construct that identifies multiple image manifests for different computer platforms (such as x86-64 or ARM 64-bit) or media types. For more information, see the [OCI Image Index Specification](https://github.com/opencontainers/image-spec/blob/main/image-index.md).
+ **Manifest:** A JSON document that defines an image or artifact that is uploaded through the manifest's endpoint. A manifest can reference other blobs in a repository by using descriptors. For more information, see the [OCI Image Manifest Specification](https://github.com/opencontainers/image-spec/blob/main/manifest.md).
+ **Filesystem layer:** System libraries and other dependencies for an image.
+ **Configuration:** A blob that contains artifact metadata and is referenced in the manifest. For more information, see the [OCI Image Configuration Specification](https://github.com/opencontainers/image-spec/blob/main/config.md).
+ **Object or artifact:** A conceptual content item that's stored as a blob and associated with an accompanying manifest with a configuration.
+ **Digest:** A unique identifier that's created from a cryptographic hash of the contents of a manifest. The image digest helps uniquely identify an immutable container image. When you pull an image by using its digest, you will download the same image every time on any operating system or architecture. For more information, see the [OCI Image Specification](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests).
+ **Tag:** A human-readable manifest identifier. Compared with image digests, which are immutable, tags are dynamic. A tag that points to an image can change and move from one image to another, although the underlying image digest remains the same.

**Target architecture**

The following diagram displays the high-level architecture of the solution provided by this pattern to identify duplicate container images by comparing images that are stored in Amazon ECR and private repositories.

![Automatically detecting duplicates with CodePipeline and CodeBuild.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7db5020c-6f5b-4e91-b91a-5b8ae844be1b/images/5ee62bc8-db8d-48a3-9e79-f3392b6e9bf7.png)

## Tools
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-tools"></a>

**AWS services**
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.

**Code **

The code for this pattern is available in the GitHub repository** **[Automated solution to identify duplicate container images between repositories](https://github.com/aws-samples/automated-solution-to-identify-duplicate-container-images-between-repositories/).

## Best practices
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-best-practices"></a>
+ [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
+ [AWS CodePipeline best practices](https://docs.aws.amazon.com/codepipeline/latest/userguide/best-practices.html)

## Epics
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-epics"></a>

### Pull container images from Amazon ECR public and private repositories
<a name="pull-container-images-from-ecr-public-and-private-repositories"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Pull an image from the Amazon ECR public repository. | From the terminal, run the following command to pull the image `amazonlinux` from the Amazon ECR public repository.<pre>$~ % docker pull public.ecr.aws/amazonlinux/amazonlinux:2018.03 </pre><br />When the image has been pulled to your local machine, you’ll see the following pull digest, which represents the image index.<pre>2018.03: Pulling from amazonlinux/amazonlinux<br />4ddc0f8d367f: Pull complete <br /><br />Digest: sha256:f972d24199508c52de7ad37a298bda35d8a1bd7df158149b381c03f6c6e363b5<br /><br />Status: Downloaded newer image for public.ecr.aws/amazonlinux/amazonlinux:2018.03<br />public.ecr.aws/amazonlinux/amazonlinux:2018.03</pre> | App developer, AWS DevOps, AWS administrator |
| Push the image to an Amazon ECR private repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html) | AWS administrator, AWS DevOps, App developer |
| Pull the same image from the Amazon ECR private repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html) | App developer, AWS DevOps, AWS administrator |

### Compare the image manifests
<a name="compare-the-image-manifests"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Find the manifest of the image stored in the Amazon ECR public repository. | From the terminal, run the following command to pull the manifest of the image `public.ecr.aws/amazonlinux/amazonlinux:2018.03` from the Amazon ECR public repository.<pre>$~ % docker manifest inspect public.ecr.aws/amazonlinux/amazonlinux:2018.03<br />{<br />   "schemaVersion": 2,<br />   "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",<br />   "manifests": [<br />      {<br />         "mediaType": "application/vnd.docker.distribution.manifest.v2+json",<br />         "size": 529,<br />         "digest": "sha256:52db9000073d93b9bdee6a7246a68c35a741aaade05a8f4febba0bf795cdac02",<br />         "platform": {<br />            "architecture": "amd64",<br />            "os": "linux"<br />         }<br />      }<br />   ]<br />}</pre> | AWS administrator, AWS DevOps, App developer |
| Find the manifest of the image stored in the Amazon ECR private repository. | From the terminal, run the following command to pull the manifest of the image `<account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository:latest` from the Amazon ECR private repository.<pre>$~ % docker manifest inspect <account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository:latest                                          <br />{<br />	"schemaVersion": 2,<br />	"mediaType": "application/vnd.docker.distribution.manifest.v2+json",<br />	"config": {<br />		"mediaType": "application/vnd.docker.container.image.v1+json",<br />		"size": 1477,<br />		"digest": "sha256:f7cee5e1af28ad4e147589c474d399b12d9b551ef4c3e11e02d982fce5eebc68"<br />	},<br />	"layers": [<br />		{<br />			"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",<br />			"size": 62267075,<br />			"digest": "sha256:4ddc0f8d367f424871a060e2067749f32bd36a91085e714dcb159952f2d71453"<br />		}<br />	]<br />}</pre> | AWS DevOps, AWS systems administrator, App developer |
| Compare the digest pulled by Docker with the manifest digest for the image in the Amazon ECR private repository. | Another question is why the digest provided by the **docker pull** command differs from the manifest's digest for the image `<account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository:latest`.<br />The digest used for **docker pull** represents the digest of the image manifest, which is stored in a registry. This digest is considered the root of a hash chain, because the manifest contains the hash of the content that will be downloaded and imported into Docker.<br />The image ID used within Docker can be found in this manifest as `config.digest`. This represents the image configuration that Docker uses. So you could say that the manifest is the envelope, and the image is the content of the envelope. The manifest digest is always different from the image ID. However, a specific manifest should always produce the same image ID. Because the manifest digest is a hash chain, we cannot guarantee that it will always be the same for a given image ID. In most cases, it produces the same digest, although Docker cannot guarantee that. The possible difference in the manifest digest stems from Docker not storing the blobs that are compressed with gzip locally. Therefore, exporting layers might produce a different digest, although the uncompressed content remains the same. The image ID verifies that uncompressed content is the same; that is, the image ID is now a content addressable identifier (`chainID`).<br />To confirm this information, you can compare the output of the **docker inspect** command on the Amazon ECR public and private repositories:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html)<br />The results verify that both images have the same image ID digest and layer digest.<br />ID: `f7cee5e1af28ad4e147589c474d399b12d9b551ef4c3e11e02d982fce5eebc68`<br />Layers: `d5655967c2c4e8d68f8ec7cf753218938669e6c16ac1324303c073c736a2e2a2`<br />Additionally, the digests are based on the bytes of the object that's managed locally (the local file is a tar of the container image layer) or the blob that's pushed to the registry server. However, when you push the blob to a registry, the tar is compressed and the digest is computed in the compressed tar file. Therefore, the difference in the **docker pull** digest value arises from compression that is applied at the registry (Amazon ECR private or public) level.This explanation is specific to using a Docker client. You won’t see this behavior with other clients such as **nerdctl** or **Finch**, because they don’t automatically compress the image during push and pull operations. | AWS DevOps, AWS systems administrator, App developer |

### Automatically identify duplicate images between Amazon ECR public and private repositories
<a name="automatically-identify-duplicate-images-between-ecr-public-and-private-repositories"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the Github repository for this pattern into a local folder:<pre>$git clone https://github.com/aws-samples/automated-solution-to-identify-duplicate-container-images-between-repositories</pre> | AWS administrator, AWS DevOps |
| Set up a CI/CD pipeline. | The GitHub repository includes a `.yaml` file that creates an CloudFormation stack to set up a pipeline in AWS CodePipeline.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html)<br />The pipeline will be set up with two stages (CodeCommit and CodeBuild, as shown in the architecture diagram) to identify images in the private repository that also exist in the public repository. The pipeline is configured with the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html) | AWS administrator, AWS DevOps |
| Populate the CodeCommit repository. | To populate the CodeCommit repository, perform these steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html) | AWS administrator, AWS DevOps |
| Clean up. | To avoid incurring future charges, delete the resources by following these steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html) | AWS administrator |

## Troubleshooting
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| When you try to push, pull, or otherwise interact with a CodeCommit repository from the terminal or command line, you are prompted to provide a user name and password, and you must supply the Git credentials for your IAM user. | The most common causes for this error are the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html)<br />Depending on your operating system and local environment, you might need to install a credential manager, configure the credential manager that is included in your operating system, or customize your local environment to use credential storage. For example, if your computer is running macOS, you can use the Keychain Access utility to store your credentials. If your computer is running Windows, you can use the Git Credential Manager that is installed with Git for Windows. For more information, see [Setup for HTTPS users using Git credentials](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html) in the CodeCommit documentation and [Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) in the Git documentation. |
| You encounter HTTP 403 or "no basic auth credentials" errors when you push an image to the Amazon ECR repository. | You might encounter these error messages from the **docker push** or **docker pull** command, even if you have successfully authenticated to Docker by using the **aws ecr get-login-password** command. Known causes are:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository.html) |

## Related resources
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-resources"></a>
+ [Automated solution to identify duplicate container images between repositories](https://github.com/aws-samples/automated-solution-to-identify-duplicate-container-images-between-repositories/) (GitHub repository)
+ [Amazon ECR public gallery](https://gallery.ecr.aws/)
+ [Private images in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images.html) (Amazon ECR documentation)
+ [AWS::CodePipeline::Pipeline resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html) (CloudFormation documentation)
+ [OCI Image Format Specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)

## Additional information
<a name="identify-duplicate-container-images-automatically-when-migrating-to-ecr-repository-additional"></a>

**Output of Docker inspection for image in Amazon ECR public repository**

```
[
    {
        "Id": "sha256:f7cee5e1af28ad4e147589c474d399b12d9b551ef4c3e11e02d982fce5eebc68",
        "RepoTags": [
            "<account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository:latest",
            "public.ecr.aws/amazonlinux/amazonlinux:2018.03"
        ],
        "RepoDigests": [
            "<account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository@sha256:52db9000073d93b9bdee6a7246a68c35a741aaade05a8f4febba0bf795cdac02",
            "public.ecr.aws/amazonlinux/amazonlinux@sha256:f972d24199508c52de7ad37a298bda35d8a1bd7df158149b381c03f6c6e363b5"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-02-23T06:20:11.575053226Z",
        "Container": "ec7f2fc7d2b6a382384061247ef603e7d647d65f5cd4fa397a3ccbba9278367c",
        "ContainerConfig": {
            "Hostname": "ec7f2fc7d2b6",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/bin/bash\"]"
            ],
            "Image": "sha256:c1bced1b5a65681e1e0e52d0a6ad17aaf76606149492ca0bf519a466ecb21e51",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "DockerVersion": "20.10.17",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "sha256:c1bced1b5a65681e1e0e52d0a6ad17aaf76606149492ca0bf519a466ecb21e51",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 167436755,
        "VirtualSize": 167436755,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/c2c2351a82b26cbdf7782507500e5adb5c2b3a2875bdbba79788a4b27cd6a913/merged",
                "UpperDir": "/var/lib/docker/overlay2/c2c2351a82b26cbdf7782507500e5adb5c2b3a2875bdbba79788a4b27cd6a913/diff",
                "WorkDir": "/var/lib/docker/overlay2/c2c2351a82b26cbdf7782507500e5adb5c2b3a2875bdbba79788a4b27cd6a913/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:d5655967c2c4e8d68f8ec7cf753218938669e6c16ac1324303c073c736a2e2a2"
            ]
        },
        "Metadata": {
            "LastTagTime": "2023-03-02T10:28:47.142155987Z"
        }
    }
]
```

**Output of Docker inspection for image in Amazon ECR private repository**

```
[
    {
        "Id": "sha256:f7cee5e1af28ad4e147589c474d399b12d9b551ef4c3e11e02d982fce5eebc68",
        "RepoTags": [
            "<account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository:latest",
            "public.ecr.aws/amazonlinux/amazonlinux:2018.03"
        ],
        "RepoDigests": [
            "<account-id>.dkr.ecr.us-east-1.amazonaws.com/test_ecr_repository@sha256:52db9000073d93b9bdee6a7246a68c35a741aaade05a8f4febba0bf795cdac02",
            "public.ecr.aws/amazonlinux/amazonlinux@sha256:f972d24199508c52de7ad37a298bda35d8a1bd7df158149b381c03f6c6e363b5"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-02-23T06:20:11.575053226Z",
        "Container": "ec7f2fc7d2b6a382384061247ef603e7d647d65f5cd4fa397a3ccbba9278367c",
        "ContainerConfig": {
            "Hostname": "ec7f2fc7d2b6",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/bin/bash\"]"
            ],
            "Image": "sha256:c1bced1b5a65681e1e0e52d0a6ad17aaf76606149492ca0bf519a466ecb21e51",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "DockerVersion": "20.10.17",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "sha256:c1bced1b5a65681e1e0e52d0a6ad17aaf76606149492ca0bf519a466ecb21e51",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 167436755,
        "VirtualSize": 167436755,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/c2c2351a82b26cbdf7782507500e5adb5c2b3a2875bdbba79788a4b27cd6a913/merged",
                "UpperDir": "/var/lib/docker/overlay2/c2c2351a82b26cbdf7782507500e5adb5c2b3a2875bdbba79788a4b27cd6a913/diff",
                "WorkDir": "/var/lib/docker/overlay2/c2c2351a82b26cbdf7782507500e5adb5c2b3a2875bdbba79788a4b27cd6a913/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:d5655967c2c4e8d68f8ec7cf753218938669e6c16ac1324303c073c736a2e2a2"
            ]
        },
        "Metadata": {
            "LastTagTime": "2023-03-02T10:28:47.142155987Z"
        }
    }
]
```
