document.addEventListener('alpine:init', () => {
    Alpine.data('showMenu', () => ({
        open: false,
    }))
})