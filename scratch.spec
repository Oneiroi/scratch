Name: scratch	
Version:	1.4.0.6
Release:	1%{?dist}
Summary:	Scratch is a programming language that makes it easy to create your own interactive stories, animations, games, music, and art -- and share your creations on the web.

Group:	Development/Tools	
License:	GPLv2
URL:		http://scratch.mit.edu/
Source0:	scratch-%{version}.src.tar.gz

BuildRequires:    libv4l, lib4vl-devel	
Requires:	squeak

%description

Scratch is a programming language that makes it easy to create your own interactive stories, animations, games, music, and art -- and share your creations on the web.

As young people create and share Scratch projects, they learn important mathematical and computational ideas, while also learning to think creatively, reason systematically, and work collaboratively.

Scratch is developed by the Lifelong Kindergarten Group at the MIT Media Lab, with financial support from the National Science Foundation, Microsoft, Intel Foundation, MacArthur Foundation, Google, Iomega and MIT Media Lab research consortia.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

