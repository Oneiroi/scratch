VERSION = 1.4.0.6
RELEASE = 1
git_head	= $(shell git log -1 --pretty=format:%h)
date		= $(shell date --utc +%Y%m%d%H%M%S)
GIT_RELEASE	= $(date)git$(git_head)
RPMDIR		= $$(rpm --eval '%{_rpmdir}')

dist-spec:
	sed -e "s|@VERSION@|$(VERSION)|;s|^\(Release:[^%]*\)|\1$(RELEASE)|" scratch.spec.in > scracth.spec
	
test-spec:
	sed -e "s|@VERSION@|$(VERSION)|;s|^\(Release:[^%]*\)|\1$(GIT_RELEASE)" scratch.spec.in > scratch.spec

build:
	mkdir -p dist/scratch-$(VERSION)
	$(shell [[ -f "scratch-$(VERSION).src.tar.gz" ]] || \
		([[ -x "/usr/bin/curl" ]] && /usr/bin/curl -o scratch-$(VERSION).src.tar.gz \
		http://download.scratch.mit.edu/%{name}-%{version}.src.tar.gz || echo "curl not installed?")
	)
	cp -a -r scratch.spec dist/
	tar ---update scratch-$(VERSION).src.tar.gz scratch.spec
test: test-spec build
dist: dist-spec build

dist-rpms: dist
	rpmbuild $(RPM_FLAGS) -ta scratch-$(VERSION).tar.gz

dist-test: test
	rpmbuild $(RPM_FLAGS) -ta scratch-$(VERSION).tar.gz

clean:
	rm -rf scratch-$(VERSION).src.tar.gz scratch.spec