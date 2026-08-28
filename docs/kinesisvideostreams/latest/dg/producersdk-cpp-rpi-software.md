---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-software.html
---

# Install software prerequisites
<a name="producersdk-cpp-rpi-software"></a>

The C\+\+ producer SDK requires that you install the following software prerequisites on Raspberry Pi.

1. Update the package list and install the libraries needed to build the SDK. Open the terminal and type the following commands:

   ```
   sudo apt-get update
   sudo apt-get install -y \
     automake \
     build-essential \
     cmake \
     git \
     gstreamer1.0-plugins-base-apps \
     gstreamer1.0-plugins-bad \
     gstreamer1.0-plugins-good \
     gstreamer1.0-plugins-ugly \
     gstreamer1.0-tools \
     gstreamer1.0-omx-generic \
     libcurl4-openssl-dev \
     libgstreamer1.0-dev \
     libgstreamer-plugins-base1.0-dev \
     liblog4cplus-dev \
     libssl-dev \
     pkg-config
   ```

1. If you’re using the `libcamera` stack, also install the `libcamerasrc` GStreamer plugin. This GStreamer plugin doesn't come installed by default.

   ```
   sudo apt-get install gstreamer1.0-libcamera
   ```

1. Copy the following PEM file to `/etc/ssl/cert.pem`:

   ```
   sudo curl https://www.amazontrust.com/repository/AmazonRootCA1.pem -o /etc/ssl/AmazonRootCA1.pem
   sudo chmod 644 /etc/ssl/AmazonRootCA1.pem
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
