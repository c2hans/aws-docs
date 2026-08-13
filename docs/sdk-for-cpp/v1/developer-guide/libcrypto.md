---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/libcrypto.html
---

# Using a custom libcrypto library in the AWS SDK for C\+\+
<a name="libcrypto"></a>

 By default, the AWS SDK for C\+\+ uses the default system cryptographic library for transport layer security. However, the SDK for C\+\+ can optionally be configured to use a different libcrypto library when building the SDK from source. This functionally means that all cryptographic operations will be diverted to a custom implementation of OpenSSL. For example, you might want to use the [`AWS-LC`](https://github.com/aws/aws-lc) library in [FIPS mode](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/) to achieve a FIPS standard in your application.

## How to build a custom libcrypto into the SDK for C\+\+
<a name="howToBuildLibcrypto"></a>

### Step 1: Build or obtain your libcrypto library
<a name="buildObtainLibCrypto"></a>

The [`AWS-LC`](https://github.com/aws/aws-lc) is one example of an alternative libcrypto library, but any distribution of OpenSSL or OpenSSL-equivalent would work.

The SDK for C\+\+, and its dependency the CRT, both use libcrypto for their cryptographic functions and both need to handle dependencies the same. The SDK for C\+\+ depends on two different HTTP clients depending on if the request uses the SDK’s `CRT S3` functionality. The CRT specifically is dependent on [s2n](https://github.com/aws/s2n-tls), a TLS implementation that is initialized at start up time. Both the SDK and the s2n team have a cmake parameter to force the use of a shared libcrypto library regardless of the value of [BUILD\_SHARED\_LIBS](cmake-params.md#cmake-build-shared-libs). Typically, you want the CRT HTTP client and the regular HTTP client to use the same libcrypto. In this case, that would mean both referencing OpenSSL in the dependency tree. The SDK provides this via [AWS\_USE\_CRYPTO\_SHARED\_LIBS](cmake-params.md#cmake-use-crypto) and s2n (for CRT-based calls) provides this through [`S2N_USE_CRYPTO_SHARED_LIBS`](https://github.com/aws/s2n-tls/blob/20010e6b75a09ab5a0fc69a86265d3cc4c103b91/CMakeLists.txt#L39). Dependency resolution is the same between these two libraries, and typically these are set to match, though you can explicitly set them to be different.

For example, to use `AWS-LC` as the libcrypto library, you would build it as follows:

```
git clone --depth 1 -b fips-2022-11-02 https://github.com/aws/aws-lc && \
    cd aws-lc && \
    mkdir build && \
    cd build && \
    cmake -G Ninja \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_PREFIX=/lc-install .. && \
    cmake --build . && \
    cmake --install . && \
    rm -rf ./* && \
    cmake -G Ninja \
        -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_PREFIX=/lc-install .. && \
    cmake --build . && \
    cmake --install .
```

### Step 2: Build curl from source or use a curl distribution with your libcrypto library
<a name="BuildCurlWithLibCrypto"></a>

The SDK for C\+\+ requires that an HTTP client is installed on the system that will be used to make HTTP requests. The HTTP client must be built with the libcrypto that you intend to use. The HTTP client is responsible for TLS operations and, thus, uses your libcrypto library.

 In the following example, the curl library is rebuilt using an installed version of `AWS-LC`.

```
git clone --depth 1 -b curl-8_5_0 https://github.com/curl/curl && \
    cd curl && \
    autoreconf -fi && \
    mkdir build && \
    cd build && \
    ../configure \
        --enable-warnings \
        --enable-werror \
        --with-openssl=/lc-install \
        --prefix=/curl-install && \
    make && \
    make install
```

### Step 3: Build the SDK using libcrypto and curl libraries
<a name="BuildUsingLibcryptoCurl"></a>

The SDK for C\+\+ can now be built using the previously created libcrypto and curl artifacts. This build of the SDK will use the custom libcrypto library for all cryptographic functionality.

```
git clone --depth 1 --recurse-submodules https://github.com/aws/aws-sdk-cpp \
    cd aws-sdk-cpp && \
    mkdir build && \
    cd build && \
    cmake -G Ninja \
        -DCMAKE_PREFIX_PATH="/curl-install;/lc-install;" \
        -DBUILD_ONLY="s3" \
        -DCMAKE_INSTALL_PREFIX=/sdk-install \
        -DAUTORUN_UNIT_TESTS=OFF .. && \
    cmake --build . && \
    cmake --install .
```

## Bringing it all together in a docker image
<a name="dockerImageForLibcrypto"></a>

The following sample Docker file shows how to implement these steps in Amazon Linux 2023 environment.

```

# User AL2023 Base image
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# Install Dev Tools
RUN yum groupinstall -y "Development Tools"
RUN yum install -y cmake3 ninja-build

# Build and install AWS-LC on the fips branch both statically and dynamically.
RUN git clone --depth 1 -b fips-2022-11-02 https://github.com/aws/aws-lc && \\
    cd aws-lc && \\
    mkdir build && \\
    cd build && \\
    cmake -G Ninja \\
        -DCMAKE_INSTALL_LIBDIR=lib \\
        -DCMAKE_INSTALL_PREFIX=/lc-install .. && \\
    cmake --build . && \\
    cmake --install . && \\
    rm -rf ./* && \\
    cmake -G Ninja \\
        -DBUILD_SHARED_LIBS=ON \\
        -DCMAKE_INSTALL_LIBDIR=lib \\
        -DCMAKE_INSTALL_PREFIX=/lc-install .. && \\
    cmake --build . && \\
    cmake --install .

# Build and install curl targeting AWS-LC as openssl
RUN git clone --depth 1 -b curl-8_5_0 https://github.com/curl/curl && \\
    cd curl && \\
    autoreconf -fi && \\
    mkdir build && \\
    cd build && \\
    ../configure \\
        --enable-warnings \\
        --enable-werror \\
        --with-openssl=/lc-install \\
        --prefix=/curl-install && \\
    make && \\
    make install

# Build and install SDK using the Curl and AWS-LC targets previously built
RUN git clone --depth 1 --recurse-submodules https://github.com/aws/aws-sdk-cpp \\
    cd aws-sdk-cpp && \\
    mkdir build && \\
    cd build && \\
    cmake -G Ninja \\
        -DCMAKE_PREFIX_PATH="/curl-install;/lc-install;" \\
        -DBUILD_ONLY="s3" \\
        -DCMAKE_INSTALL_PREFIX=/sdk-install \\
        -DAUTORUN_UNIT_TESTS=OFF .. && \\
    cmake --build . && \\
    cmake --install .
```
