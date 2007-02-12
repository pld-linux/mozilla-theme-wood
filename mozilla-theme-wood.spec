Summary:	Wooden theme based on LittleMozilla
Summary(pl.UTF-8):   Drewniany motyw bazujący na LittleMozilla
Name:		mozilla-theme-wood
Version:	1.3
%define		_realname	wood
%define	_fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}_%{_fver}.jar
# Source0-md5:	9746c376253cd81f47f2f056f7f80ab3
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/wood.html
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Theme made with care for details. All browser elements are made of
wood. Small buttons and toolbars leave big workspace.

%description -l pl.UTF-8
Motyw wykonany z wielkim wyczuciem i dbałością o szczegóły. Wszystkie
elementy przeglądarki są wykonane drewna. Niewielkie przyciski i paski
narzędziowe pozwalają na maksymalne wykorzystanie przestrzeni roboczej.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
