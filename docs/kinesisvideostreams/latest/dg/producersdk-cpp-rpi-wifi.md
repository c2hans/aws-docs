---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-wifi.html
---

# Join your Raspberry Pi to your Wi-Fi network
<a name="producersdk-cpp-rpi-wifi"></a>

If you are using an attached monitor and keyboard, proceed to [Configure the Raspberry Pi camera](producersdk-cpp-rpi-camera.md).

These instructions are written to help you to set up your Raspberry Pi when run in *headless* mode, that is, without an attached keyboard, monitor, or network cable. Follow the instructions below to configure your Raspberry Pi to automatically attempt connecting to the specified network, allowing your host machine to be able to SSH into it.

1. On your computer, create a file named `wpa_supplicant.conf`.

1. Copy the following text and paste it into the `wpa_supplicant.conf` file:

   ```
   country=US
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1

   network={
   ssid="{{Your Wi-Fi SSID}}"
   scan_ssid=1
   key_mgmt=WPA-PSK
   psk="{{Your Wi-Fi Password}}"
   }
   ```

   Replace the `ssid` and `psk` values with the information for your Wi-Fi network.

1. Copy the `wpa_supplicant.conf` file to the SD card. It must be copied to the root of the `boot` volume.

1. Insert the SD card into the Raspberry Pi, and power the device. It joins your Wi-Fi network, and SSH is enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
