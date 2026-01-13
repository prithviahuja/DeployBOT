# Use official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root to install packages
USER root

# Install Docker CLI from Debian repos (safe for trixie)
RUN apt-get update && \
    apt-get install -y \
        ca-certificates \
        curl \
        gnupg \
        docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add jenkins user to docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Switch back to Jenkins user
USER jenkins
 