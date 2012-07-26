Name: scratch   
Version:    1.4.0.6
Release:    1%{?dist}
Summary:    Scratch is a programming language that makes it easy to create your own interactive stories, animations, games, music, and art -- and share your creations on the web.

Group:      Development/Tools   
License:    GPLv2
URL:        http://scratch.mit.edu/
Source0:    http://download.scratch.mit.edu/%{name}-%{version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}.src/

BuildRequires:  libv4l, libv4l-devel, pango, pango-devel   
Requires:   squeak, pango

%description

Scratch is a programming language that makes it easy to create your own interactive stories, animations, games, music, and art -- and share your creations on the web.

As young people create and share Scratch projects, they learn important mathematical and computational ideas, while also learning to think creatively, reason systematically, and work collaboratively.

Scratch is developed by the Lifelong Kindergarten Group at the MIT Media Lab, with financial support from the National Science Foundation, Microsoft, Intel Foundation, MacArthur Foundation, Google, Iomega and MIT Media Lab research consortia.


%prep
%setup -qn %{name}-%{version}.src


%build
make %{?_smp_mflags}


%install

install -m 755 -d %{buildroot}%{_libdir}/%{name}/App
#install -m 755 App/scratch_squeak_vm %{buildroot}%{_libdir}/%{name}/App/
install -m 644 Scratch.image %{buildroot}%{_libdir}/%{name}/
install -m 644 Scratch.ini %{buildroot}%{_libdir}/%{name}/
install -m 755 -d %{buildroot}%{_libdir}/%{name}/Plugins
install -m 644 Plugins/* %{buildroot}%{_libdir}/%{name}/Plugins/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Help/en/images
install -m 644 Help/en/*.pdf %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/*.html %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/images/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/images/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/locale
install -m 644 locale/* %{buildroot}%{_datadir}/%{name}/locale/

cp -R Media  %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Animation
install -m 644 Projects/Animation/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Animation/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Games
install -m 644 Projects/Games/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Games/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Greetings
install -m 644 Projects/Greetings/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Greetings/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art
install -m 644 Projects/Interactive\ Art/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance
install -m 644 Projects/Music\ and\ Dance/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Names
install -m 644 Projects/Names/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Names/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors
install -m 644 Projects/Sensors\ and\ Motors/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Simulations
install -m 644 Projects/Simulations/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Simulations/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up
install -m 644 Projects/Speak\ Up/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Stories
install -m 644 Projects/Stories/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Stories/

install -m 644 LICENSE %{buildroot}%{_datadir}/%{name}/
install -m 644 gpl-2.0.txt %{buildroot}%{_datadir}/%{name}/
install -m 644 ACKNOWLEDGEMENTS %{buildroot}%{_datadir}/%{name}/
install -m 644 KNOWN-BUGS %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 src/scratch %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 src/man/scratch.1.gz %{buildroot}%{_mandir}/man1/
#install -m 644 src/man/scratch_squeak_vm.1.gz %{buildroot}%{_mandir}/man1/

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 src/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 src/icons/48x48/scratch.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 644 src/icons/128x128/scratch.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -m 644 src/icons/48x48/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes
install -m 644 src/icons/128x128/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/

install -m 755 -d %{buildroot}%{_datadir}/mime/packages
install -m 644 src/%{name}.xml %{buildroot}%{_datadir}/mime/packages/

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/128x128/mimetypes/*


%doc



%changelog

* Wed Jul 11 2012 David Busby <oneiroi@fedoraproject.org> - 1.4.0.6-1
- Initial specification for project; using reference spec:http://subversion.assembla.com/svn/scratchonlinux/trunk/scratch/rpm/SPECS/scratch-1.4.0.1.spec
