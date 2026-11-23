---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-software-start-ros.html
---

# Start the ROS server

1. SSH into the Raspberry Pi:

   ```bash
   ssh deepracer@deepracer.local
   ```

1. Start the AWS DeepRacer software stack by running the provided script:

   ```bash
   sudo /opt/aws/deepracer/start_ros.sh
   ```

After the first successful run, the ROS server starts automatically on boot. You do not need to run this script manually on subsequent restarts.
