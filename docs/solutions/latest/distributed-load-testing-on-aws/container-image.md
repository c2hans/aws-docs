---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/container-image.html
---

# Container image customization
<a name="container-image"></a>

## Load tester image
<a name="load-tester-image"></a>

This solution uses a public Amazon Elastic Container Registry (Amazon ECR) image repository managed by AWS to store the image that is used to run the configured tests. If you want to customize the container image, you can rebuild and push the image into an ECR image repository in your own AWS account.

If you want to customize this solution, you can use the default container image or, edit this container to fit your needs. If you customize the solution, use the following code sample to declare the environment variables before building your customized solution.

```
#!/bin/bash
export REGION=aws-region-code # the AWS region to launch the solution (e.g. us-east-1)
export BUCKET_PREFIX=my-bucket-name # prefix of the bucket name without the region code
export BUCKET_NAME=$BUCKET_PREFIX-$REGION # full bucket name where the code will reside
export SOLUTION_NAME=my-solution-name
export VERSION=my-version # version number for the customized code
export PUBLIC_ECR_REGISTRY=public.ecr.aws/awssolutions/distributed-load-testing-on-aws-load-tester # replace with the container registry and image if you want to use a different container image export PUBLIC_ECR_TAG=v3.1.0 # replace with the container image tag if you want to use a different container image
```

If you choose to customize the container image, you can host it in either a private image repository, or a public image repository in your AWS account. The image resources are in the `deployment/ecr/distributed-load-testing-on-aws-load-tester` directory, located in the code base.

You can build and push the image to the host destination.
+ For private Amazon ECR repositories and images, refer to [Amazon ECR private repositories](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) and [private images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images.html) in the *Amazon ECR User Guide*.
+ For public Amazon ECR repositories and images, refer to [Amazon ECR public repositories](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repositories.html) and [public images](https://docs.aws.amazon.com/AmazonECR/latest/public/public-images.html) in the *Amazon ECR Public User Guide*.

Once you create your own image, you can declare the following environment variables before building your customized solution.

```
#!/bin/bash
export PUBLIC_ECR_REGISTRY=YOUR_ECR_REGISTRY_URI # e.g. YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/YOUR_IMAGE_NAME
export PUBLIC_ECR_TAG=YOUR_ECR_TAG # e.g. latest, v3.4.0
```

The following example shows the container file.

```
FROM public.ecr.aws/amazonlinux/amazonlinux:2023-minimal

RUN dnf update -y && \
    dnf install -y python3.11 python3.11-pip java-21-amazon-corretto bc procps jq findutils unzip && \
    dnf clean all

ENV PIP_INSTALL="pip3.11 install --no-cache-dir"

# install bzt
RUN $PIP_INSTALL --upgrade bzt awscli setuptools==78.1.1 h11 urllib3==2.2.2 && \
    $PIP_INSTALL --upgrade bzt
COPY ./.bzt-rc /root/.bzt-rc
RUN chmod 755 /root/.bzt-rc

# install bzt tools
RUN bzt -install-tools -o modules.install-checker.exclude=selenium,gatling,tsung,siege,ab,k6,external-results-loader,locust,junit,testng,rspec,mocha,nunit,xunit,wdio,robot,newman
RUN rm -rf /root/.bzt/selenium-taurus
RUN mkdir /bzt-configs /tmp/artifacts
ADD ./load-test.sh /bzt-configs/
ADD ./*.jar /bzt-configs/
ADD ./*.py /bzt-configs/

RUN chmod 755 /bzt-configs/load-test.sh
RUN chmod 755 /bzt-configs/ecslistener.py
RUN chmod 755 /bzt-configs/ecscontroller.py
RUN chmod 755 /bzt-configs/jar_updater.py
RUN python3.11 /bzt-configs/jar_updater.py

# Remove jar files from /tmp
RUN rm -rf /tmp/jmeter-plugins-manager-1* && \
    rm -rf /usr/local/lib/python3.11/site-packages/setuptools-65.5.0.dist-info && \
    rm -rf /usr/local/lib/python3.11/site-packages/urllib3-1.26.17.dist-info

# Add settings file to capture the output logs from bzt cli
RUN mkdir -p /etc/bzt.d && echo '{"settings": {"artifacts-dir": "/tmp/artifacts"}}' > /etc/bzt.d/90-artifacts-dir.json

WORKDIR /bzt-configs
ENTRYPOINT ["./load-test.sh"]
```

In addition to a container file, the directory contains the following bash script that downloads the test configuration from Amazon S3 before running the Taurus/Blazemeter program.

```
#!/bin/bash

# set a uuid for the results xml file name in S3
UUID=$(cat /proc/sys/kernel/random/uuid)
pypid=0
echo "S3_BUCKET:: ${S3_BUCKET}"
echo "TEST_ID:: ${TEST_ID}"
echo "TEST_TYPE:: ${TEST_TYPE}"
echo "FILE_TYPE:: ${FILE_TYPE}"
echo "PREFIX:: ${PREFIX}"
echo "UUID:: ${UUID}"
echo "LIVE_DATA_ENABLED:: ${LIVE_DATA_ENABLED}"
echo "MAIN_STACK_REGION:: ${MAIN_STACK_REGION}"

cat /proc/self/cgroup
TASK_ID=$(grep -oE '[a-f0-9]{32}' /proc/self/cgroup | head -n 1)
echo $TASK_ID

sigterm_handler() {
  if [ $pypid -ne 0 ]; then
    echo "container received SIGTERM."
    kill -15 $pypid
    wait $pypid
    exit 143 #128 + 15
  fi
}
trap 'sigterm_handler' SIGTERM

echo "Download test scenario"
aws s3 cp s3://$S3_BUCKET/test-scenarios/$TEST_ID-$AWS_REGION.json test.json --region $MAIN_STACK_REGION

# Set the default log file values to jmeter
LOG_FILE="jmeter.log"
OUT_FILE="jmeter.out"
ERR_FILE="jmeter.err"
KPI_EXT="jtl"

# download JMeter jmx file
if [ "$TEST_TYPE" != "simple" ]; then
  # setting the log file values to the test type
  LOG_FILE="${TEST_TYPE}.log"
  OUT_FILE="${TEST_TYPE}.out"
  ERR_FILE="${TEST_TYPE}.err"

  # set variables based on TEST_TYPE
  if [ "$TEST_TYPE" == "jmeter" ]; then
    EXT="jmx"
    TYPE_NAME="JMeter"
    # Copy *.jar to JMeter library path. See the Taurus JMeter path: https://gettaurus.org/docs/JMeter/
    JMETER_LIB_PATH=`find ~/.bzt/jmeter-taurus -type d -name "lib"`
    echo "cp $PWD/*.jar $JMETER_LIB_PATH"
    cp $PWD/*.jar $JMETER_LIB_PATH
  elif [ "$TEST_TYPE" == "k6" ]; then
    curl --output /tmp/artifacts/k6.rpm https://dl.k6.io/rpm/x86_64/k6-v0.58.0-amd64.rpm
    rpm -ivh /tmp/artifacts/k6.rpm
    dnf install -y k6
    rm -rf /tmp/artifacts/k6.rpm
    EXT="js"
    KPI_EXT="csv"
    TYPE_NAME="K6"
  elif [ "$TEST_TYPE" == "locust" ]; then
    EXT="py"
    TYPE_NAME="Locust"

  fi

  if [ "$FILE_TYPE" != "zip" ]; then
    aws s3 cp s3://$S3_BUCKET/public/test-scenarios/$TEST_TYPE/$TEST_ID.$EXT ./ --region $MAIN_STACK_REGION
  else
    aws s3 cp s3://$S3_BUCKET/public/test-scenarios/$TEST_TYPE/$TEST_ID.zip ./ --region $MAIN_STACK_REGION
    unzip $TEST_ID.zip
    echo "UNZIPPED"
    ls -l

    # If zip and locust, make sure to pick locustfile
    if [ "$TEST_TYPE" != "locust" ]; then
      TEST_SCRIPT=$(find . -name "*.${EXT}" | head -n 1)
    else
      TEST_SCRIPT=$(find . -name "locustfile.py" | head -n 1)
    fi
    # only looks for the first test script file.
    TEST_SCRIPT=`find . -name "*.${EXT}" | head -n 1`
    echo $TEST_SCRIPT
    if [ -z "$TEST_SCRIPT" ]; then
      echo "There is no test script (.${EXT}) in the zip file."
      exit 1
    fi

    sed -i -e "s|$TEST_ID.$EXT|$TEST_SCRIPT|g" test.json

    # copy bundled plugin jars to jmeter extension folder to make them available to jmeter
    BUNDLED_PLUGIN_DIR=`find $PWD -type d -name "plugins" | head -n 1`
    # attempt to copy only if a /plugins folder is present in upload
    if [ -z "$BUNDLED_PLUGIN_DIR" ]; then
      echo "skipping plugin installation (no /plugins folder in upload)"
    else
      # ensure the jmeter extensions folder exists
      JMETER_EXT_PATH=`find ~/.bzt/jmeter-taurus -type d -name "ext"`
      if [ -z "$JMETER_EXT_PATH" ]; then
        # fail fast - if plugins bundled they will be needed for the tests
        echo "jmeter extension path (~/.bzt/jmeter-taurus/**/ext) not found - cannot install bundled plugins"
        exit 1
      fi
      cp -v $BUNDLED_PLUGIN_DIR/*.jar $JMETER_EXT_PATH
    fi
  fi
fi

#Download python script
if [ -z "$IPNETWORK" ]; then
    python3.11 -u $SCRIPT  $TIMEOUT &
    pypid=$!
    wait $pypid
    pypid=0
else
    aws s3 cp s3://$S3_BUCKET/Container_IPs/${TEST_ID}_IPHOSTS_${AWS_REGION}.txt ./ --region $MAIN_STACK_REGION
    export IPHOSTS=$(cat ${TEST_ID}_IPHOSTS_${AWS_REGION}.txt)
    python3.11 -u $SCRIPT $IPNETWORK $IPHOSTS
fi

echo "Running test"

stdbuf -i0 -o0 -e0 bzt test.json -o modules.console.disable=true | stdbuf -i0 -o0 -e0 tee -a result.tmp | sed -u -e "s|^|$TEST_ID $LIVE_DATA_ENABLED |"
CALCULATED_DURATION=`cat result.tmp | grep -m1 "Test duration" | awk -F ' ' '{ print $5 }' | awk -F ':' '{ print ($1 * 3600) + ($2 * 60) + $3 }'`

# upload custom results to S3 if any
# every file goes under $TEST_ID/$PREFIX/$UUID to distinguish the result correctly
if [ "$TEST_TYPE" != "simple" ]; then
  if [ "$FILE_TYPE" != "zip" ]; then
    cat $TEST_ID.$EXT | grep filename > results.txt
  else
    cat $TEST_SCRIPT | grep filename > results.txt
  fi

  if [ -f results.txt ]; then
    sed -i -e 's/<stringProp name="filename">//g' results.txt
    sed -i -e 's/<\/stringProp>//g' results.txt
    sed -i -e 's/ //g' results.txt

    echo "Files to upload as results"
    cat results.txt

    files=(`cat results.txt`)
    extensions=()
    for f in "${files[@]}"; do
      ext="${f##*.}"
      if [[ ! " ${extensions[@]} " =~ " ${ext} " ]]; then
        extensions+=("$ext")
      fi
    done

    # Find all files in the current folder with the same extensions
    all_files=()
    for ext in "${extensions[@]}"; do
      for f in *."$ext"; do
        all_files+=("$f")
      done
    done

    for f in "${all_files[@]}"; do
      p="s3://$S3_BUCKET/results/$TEST_ID/${TYPE_NAME}_Result/$PREFIX/$UUID/$f"
      if [[ $f = /* ]]; then
        p="s3://$S3_BUCKET/results/$TEST_ID/${TYPE_NAME}_Result/$PREFIX/$UUID$f"
      fi

        echo "Uploading $p"
        aws s3 cp $f $p --region $MAIN_STACK_REGION
    done
    fi
fi

if [ -f /tmp/artifacts/results.xml ]; then

  # Insert the Task ID at the same level as <FinalStatus>
  curl -s $ECS_CONTAINER_METADATA_URI_V4/task
  Task_CPU=$(curl -s $ECS_CONTAINER_METADATA_URI_V4/task | jq '.Limits.CPU')
  Task_Memory=$(curl -s $ECS_CONTAINER_METADATA_URI_V4/task | jq '.Limits.Memory')
  START_TIME=$(curl -s "$ECS_CONTAINER_METADATA_URI_V4/task" | jq -r '.Containers[0].StartedAt')
  # Convert start time to seconds since epoch
  START_TIME_EPOCH=$(date -d "$START_TIME" +%s)
  # Calculate elapsed time in seconds
  CURRENT_TIME_EPOCH=$(date +%s)
  ECS_DURATION=$((CURRENT_TIME_EPOCH - START_TIME_EPOCH))

  sed -i.bak 's/<\/FinalStatus>/<TaskId>'"$TASK_ID"'<\/TaskId><\/FinalStatus>/' /tmp/artifacts/results.xml
  sed -i 's/<\/FinalStatus>/<TaskCPU>'"$Task_CPU"'<\/TaskCPU><\/FinalStatus>/' /tmp/artifacts/results.xml
  sed -i 's/<\/FinalStatus>/<TaskMemory>'"$Task_Memory"'<\/TaskMemory><\/FinalStatus>/' /tmp/artifacts/results.xml
  sed -i 's/<\/FinalStatus>/<ECSDuration>'"$ECS_DURATION"'<\/ECSDuration><\/FinalStatus>/' /tmp/artifacts/results.xml

  echo "Validating Test Duration"
  TEST_DURATION=$(grep -E '<TestDuration>[0-9]+.[0-9]+</TestDuration>' /tmp/artifacts/results.xml | sed -e 's/<TestDuration>//' | sed -e 's/<\/TestDuration>//')

  if (( $(echo "$TEST_DURATION > $CALCULATED_DURATION" | bc -l) )); then
    echo "Updating test duration: $CALCULATED_DURATION s"
    sed -i.bak.td 's/<TestDuration>[0-9]*\.[0-9]*<\/TestDuration>/<TestDuration>'"$CALCULATED_DURATION"'<\/TestDuration>/' /tmp/artifacts/results.xml
  fi

  if [ "$TEST_TYPE" == "simple" ]; then
    TEST_TYPE="jmeter"
  fi

  echo "Uploading results, bzt log, and JMeter log, out, and err files"
  aws s3 cp /tmp/artifacts/results.xml s3://$S3_BUCKET/results/${TEST_ID}/${PREFIX}-${UUID}-${AWS_REGION}.xml --region $MAIN_STACK_REGION
  aws s3 cp /tmp/artifacts/bzt.log s3://$S3_BUCKET/results/${TEST_ID}/bzt-${PREFIX}-${UUID}-${AWS_REGION}.log --region $MAIN_STACK_REGION
  aws s3 cp /tmp/artifacts/$LOG_FILE s3://$S3_BUCKET/results/${TEST_ID}/${TEST_TYPE}-${PREFIX}-${UUID}-${AWS_REGION}.log --region $MAIN_STACK_REGION
  aws s3 cp /tmp/artifacts/$OUT_FILE s3://$S3_BUCKET/results/${TEST_ID}/${TEST_TYPE}-${PREFIX}-${UUID}-${AWS_REGION}.out --region $MAIN_STACK_REGION
  aws s3 cp /tmp/artifacts/$ERR_FILE s3://$S3_BUCKET/results/${TEST_ID}/${TEST_TYPE}-${PREFIX}-${UUID}-${AWS_REGION}.err --region $MAIN_STACK_REGION
  aws s3 cp /tmp/artifacts/kpi.${KPI_EXT} s3://$S3_BUCKET/results/${TEST_ID}/kpi-${PREFIX}-${UUID}-${AWS_REGION}.${KPI_EXT} --region $MAIN_STACK_REGION

else
  echo "An error occurred while the test was running."
fi
```

In addition to the [Dockerfile](https://docs.docker.com/engine/reference/builder/) and the bash script, two Python scripts are also included in the directory. Each task runs a Python script from within the bash script. The worker tasks run the `ecslistener.py` script, while the leader task will run the `ecscontroller.py` script. The `ecslistener.py` script creates a socket on port 50000 and waits for a message. The `ecscontroller.py` script connects to the socket and sends the start test message to the worker tasks, which allows them to start simultaneously.

## Web console image (ALB \+ ECS Fargate template only)
<a name="web-console-image"></a>

The ALB \+ ECS Fargate template runs the web console as a container on ECS Fargate. By default, the solution pulls the web console image from a public Amazon ECR repository managed by AWS.

In environments where access to public container registries is restricted (for example, VPCs with no internet access or accounts with ECR public access policies), you must mirror the public image to a private Amazon ECR repository and provide the private image URI in the **Web Console Image URI** CloudFormation parameter. You can also use this approach to customize the web console image to fit your needs.

### Mirror the public image to a private ECR repository
<a name="mirror-the-public-image-to-a-private-ecr-repository"></a>

To mirror the web console image to a private ECR repository:

1. Authenticate to the public ECR registry:

   ```
   $ aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

1. Pull the public web console image:

   ```
   $ docker pull public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-web-console:<version>
   ```

1. Create a private ECR repository in your account (if one does not already exist):

   ```
   $ aws ecr create-repository --repository-name <your-repo-name> --region <region> 2>/dev/null || true
   ```

1. Authenticate to your private ECR registry:

   ```
   $ aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
   ```

1. Tag and push the image to your private repository:

   ```
   $ docker tag public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-web-console:<version> \
     <account-id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:<version>
   $ docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:<version>
   ```

1. When launching the ALB \+ ECS Fargate stack, enter the private image URI in the **Web Console Image URI** parameter:

   ```
   <account-id>.dkr.ecr.<region>.amazonaws.com/<your-repo-name>:<version>
   ```

### Customize the web console image
<a name="customize-the-web-console-image"></a>

You can also customize the web console image. The image resources are in the `deployment/ecr/distributed-load-testing-on-aws-web-console` directory, located in the [GitHub repository](https://github.com/aws-solutions/distributed-load-testing-on-aws/tree/main/deployment/ecr/distributed-load-testing-on-aws-web-console). Edit the container files to fit your needs, build the image locally, push it to your private ECR repository, and provide the URI in the **Web Console Image URI** parameter.

The web console container uses Nginx to serve the static web application. At startup, the entrypoint script downloads the web console assets from Amazon S3 and extracts them into the Nginx document root.

The following example shows the container file.

```
FROM public.ecr.aws/nginx/nginx:alpine

# Install AWS CLI for S3 operations
RUN apk upgrade --no-cache zlib libpng && \
    apk add --no-cache aws-cli

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
```

The entrypoint script downloads the web console assets from S3 and starts Nginx.

```
#!/bin/sh
set -e

S3_URI="s3://${S3_BUCKET}/${S3_KEY}"

echo "[$(date -Iseconds)] Downloading from $S3_URI"

# AWS CLI has built-in retry with exponential backoff (standard mode)
AWS_MAX_ATTEMPTS=5 aws s3 cp "$S3_URI" /tmp/web-app.zip

echo "[$(date -Iseconds)] Download successful"

# Extract and cleanup
unzip -o /tmp/web-app.zip -d /usr/share/nginx/html/
rm -f /tmp/web-app.zip

# Start Nginx
exec nginx -g 'daemon off;'
```

The Nginx configuration serves the single-page application (SPA) with health check support for the ALB, gzip compression, static asset caching, and security headers.

```
events {
  worker_connections 1024;
}

http {
  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  gzip on;
  gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

  server {
    listen 80;
    root /usr/share/nginx/html;
    index index.html;

    # Health check endpoint for ALB
    location /healthz {
      return 200 'OK';
    }

    # SPA routing
    location / {
      try_files $uri $uri/ /index.html;
    }

    # Cache static assets for 1 year
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2)$ {
      expires 1y;
      add_header Cache-Control "public, immutable";
    }

    # No cache for index.html (SPA entry point)
    location = /index.html {
      add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # No cache for runtime config
    location = /aws-exports.json {
      add_header Cache-Control "no-store, no-cache, must-revalidate";
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
  }
}
```

For more information, see [Pushing a Docker image to an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the *Amazon ECR User Guide*.

## Load tester image URI
<a name="load-tester-image-uri"></a>

All three deployment templates (Amazon CloudFront \+ S3, Application Load Balancer (ALB) \+ ECS on AWS Fargate, and headless) pull a load tester container image from the Amazon Elastic Container Registry (Amazon ECR) public registry (`public.ecr.aws`) at deploy time.

In environments where access to public container registries is restricted, mirror the load tester image to a private Amazon ECR repository and provide the private image URI in the **Load Tester Image URI** (`LoadTesterImageUri`) AWS CloudFormation parameter. Common examples include VPCs with no internet access, accounts with ECR public access policies, and AWS GovCloud (US) Regions, where ECS tasks cannot access the public ECR registry. Mirroring to a private repository in your deployment Region is required for AWS GovCloud (US) deployments and optional elsewhere.

### Mirror the load tester image to a private ECR repository
<a name="mirror-the-load-tester-image-to-a-private-ecr-repository"></a>

**Note**
When you provide `LoadTesterImageUri`, the **Auto-update Container Image** (`UseStableTagging`) parameter no longer manages the load tester image. To pick up security patches, you must re-mirror updated image tags.

To mirror the load tester image to a private ECR repository, complete the following steps. In the following commands, replace `<version>` with the image tag (for example, `v4.0.0`), `<region>` with your deployment Region (for example, `us-gov-west-1`), `<profile>` with your AWS Command Line Interface (AWS CLI) profile name, and `<account-id>` with your 12-digit AWS account ID.

1. Authenticate to the public ECR registry from a machine with internet access.

   ```
   aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

1. Pull the public load tester image.

   ```
   docker pull public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-load-tester:<version>
   ```

1. Create a private ECR repository in your account (if one does not already exist).

   ```
   aws ecr create-repository --repository-name dlt-load-tester --region <region> --profile <profile> 2>/dev/null || true
   ```

1. Authenticate to your private ECR registry.

   ```
   aws ecr get-login-password --region <region> --profile <profile> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
   ```

1. Tag and push the image to your private repository.

   ```
   docker tag public.ecr.aws/aws-solutions/distributed-load-testing-on-aws-load-tester:<version> \
     <account-id>.dkr.ecr.<region>.amazonaws.com/dlt-load-tester:<version>
   docker push <account-id>.dkr.ecr.<region>.amazonaws.com/dlt-load-tester:<version>
   ```

1. Enter the private image URI in the **Load Tester Image URI** parameter when you launch the stack.

   ```
   <account-id>.dkr.ecr.<region>.amazonaws.com/dlt-load-tester:<version>
   ```

### AWS GovCloud (US) deployment examples
<a name="aws-govcloud-us-deployment-examples"></a>

The following examples show the parameters required for each stack variant in AWS GovCloud (US).

For the headless stack, only `LoadTesterImageUri` is required:

```
aws cloudformation create-stack \
  --stack-name dlt-govcloud \
  --template-url https://solutions-reference-us-gov.s3.us-gov-west-1.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-headless.template \
  --parameters \
    ParameterKey=AdminName,ParameterValue=admin \
    ParameterKey=AdminEmail,ParameterValue=admin@example.com \
    ParameterKey=LoadTesterImageUri,ParameterValue=<account-id>.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-load-tester:<version> \
  --capabilities CAPABILITY_IAM \
  --region us-gov-west-1
```

For the Application Load Balancer (ALB) \+ ECS on AWS Fargate stack, provide both `LoadTesterImageUri` and `WebConsoleImageUri`. ECS tasks in AWS GovCloud (US) cannot access the public ECR registry (`public.ecr.aws`), so you must mirror both container images.

```
aws cloudformation create-stack \
  --stack-name dlt-govcloud \
  --template-url https://solutions-reference-us-gov.s3.us-gov-west-1.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-alb-ecs.template \
  --parameters \
    ParameterKey=AdminName,ParameterValue=admin \
    ParameterKey=AdminEmail,ParameterValue=admin@example.com \
    ParameterKey=ConsoleDomainName,ParameterValue=dlt.example.gov \
    ParameterKey=ACMCertificateArn,ParameterValue=arn:aws-us-gov:acm:us-gov-west-1:123456789012:certificate/abcd1234-ef56-gh78-ij90-klmnopqrstuv \
    ParameterKey=LoadTesterImageUri,ParameterValue=<account-id>.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-load-tester:<version> \
    ParameterKey=WebConsoleImageUri,ParameterValue=<account-id>.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-web-console:<version> \
  --capabilities CAPABILITY_IAM \
  --region us-gov-west-1
```

For instructions on mirroring the web console image, see [Web console image](#web-console-image).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
