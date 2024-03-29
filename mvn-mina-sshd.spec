#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mina-sshd
Version  : 1.6.0
Release  : 3
URL      : https://github.com/apache/mina-sshd/archive/sshd-1.6.0.tar.gz
Source0  : https://github.com/apache/mina-sshd/archive/sshd-1.6.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/sshd/sshd/1.6.0/sshd-1.6.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: mvn-mina-sshd-data = %{version}-%{release}

%description
![Apache MINA SSHD](https://mina.apache.org/staticresources/images/header-sshd.png "Apache MINA SSHD")
# Apache MINA SSHD

%package data
Summary: data components for the mvn-mina-sshd package.
Group: Data

%description data
data components for the mvn-mina-sshd package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/sshd/sshd-core/1.6.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/sshd/sshd-core/1.6.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/sshd/sshd/1.6.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/sshd/sshd/1.6.0/sshd-1.6.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.jar
/usr/share/java/.m2/repository/org/apache/sshd/sshd-core/1.6.0/sshd-core-1.6.0.pom
/usr/share/java/.m2/repository/org/apache/sshd/sshd/1.6.0/sshd-1.6.0.pom
