---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

Before deploying this solution, ensure the following prerequisites are met.

## Git LFS
<a name="git-lfs-requirement"></a>

This solution includes a pre-built container image at `deployment/container/prebid-server.tar.gz` tracked via [Git Large File Storage (LFS)](https://git-lfs.com/). If you plan to use the pre-built container image instead of building from source, you must install Git LFS before cloning the repository.

**Note**
Without Git LFS installed, the `prebid-server.tar.gz` file will be a small pointer file (\~130 bytes) rather than the actual container image. If you have already cloned the repository without Git LFS, run `git lfs pull` to download the binary file.

 **Install Git LFS:**

```
# macOS (Homebrew)
brew install git-lfs

# Amazon Linux 2023 / RHEL
sudo dnf install git-lfs

# Ubuntu / Debian
sudo apt-get install git-lfs

# Initialize Git LFS (one-time setup)
git lfs install
```

After installing Git LFS, clone the repository normally. LFS files download automatically during `git clone`.

If you prefer to build the container image from source (the default behavior when no `--container-image` flag is provided to `deploy.sh`), Git LFS is not required.

## RTB Fabric region availability
<a name="rtb-fabric-region-availability"></a>

AWS RTB Fabric is not available in all AWS Regions. If you plan to deploy with RTB Fabric connectivity for the bidder simulator, verify that your target Region supports RTB Fabric before deployment.

**Important**
If RTB Fabric is not available in your target Region, use VPC peering as the fallback connectivity mode. The `deploy.sh` script supports both modes via the `--simulator-connectivity` flag:
 `rtb-fabric` — Uses RTB Fabric Requester and Responder Gateways with a Fabric Link (recommended where available)
 `vpc-peering` — Uses VPC peering between the Prebid Server VPC and the Bidder Simulator VPC (fallback for non-RTB regions)

For the latest list of supported Regions, see the [AWS RTB Fabric product page](https://aws.amazon.com/rtb-fabric/).
