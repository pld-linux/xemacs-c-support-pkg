Summary:	Basic single-file add-ons for editing C code
Summary(pl.UTF-8):	Podstawowe dodatki do edycji kodu w C
Name:		xemacs-c-support-pkg
%define 	srcname	c-support
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	f60b46ed4078e6eda56fcb5f600f40a4
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-cc-mode-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic single-file add-ons for editing C code.

%description -l pl.UTF-8
Podstawowe dodatki do edycji kodu w C.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/c-support/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
