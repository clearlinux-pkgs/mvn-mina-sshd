PKG_NAME := mvn-mina-sshd
URL = https://github.com/apache/mina-sshd/archive/sshd-1.6.0.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/org/apache/sshd/sshd/1.6.0/sshd-1.6.0.pom : https://repo1.maven.org/maven2/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.pom : https://repo1.maven.org/maven2/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.jar :

include ../common/Makefile.common
