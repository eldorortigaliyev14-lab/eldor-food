(() => {
    const filterButtons = document.querySelectorAll('.category-button');
    const cards = document.querySelectorAll('.product-card');
    const emptyMessage = document.querySelector('.empty-menu');
    const cartButton = document.querySelector('.cart-fab');
    const cartPanel = document.querySelector('.cart-panel');
    const cartOverlay = document.querySelector('.cart-overlay');
    const cartClose = document.querySelector('.cart-close');
    const cartItems = document.querySelector('.cart-items');
    const cartTotal = document.querySelector('.cart-total strong');
    const cart = new Map();
    const formatPrice = (price) => new Intl.NumberFormat('uz-UZ').format(price);

    const filterMenu = (filter) => {
        let visibleCount = 0;
        cards.forEach((card) => {
            const visible = filter === 'all' || card.dataset.category === filter;
            card.hidden = !visible;
            if (visible) visibleCount += 1;
        });
        filterButtons.forEach((button) => {
            button.classList.toggle('selected', button.dataset.filter === filter);
        });
        emptyMessage.hidden = visibleCount > 0;
    };

    filterButtons.forEach((button) => {
        button.addEventListener('click', () => filterMenu(button.dataset.filter));
    });

    document.querySelectorAll('[data-category-jump]').forEach((link) => {
        link.addEventListener('click', () => filterMenu(link.dataset.categoryJump));
    });

    const renderCart = () => {
        const quantity = [...cart.values()].reduce((sum, item) => sum + item.quantity, 0);
        const sum = [...cart.values()].reduce((value, item) => value + item.price * item.quantity, 0);
        document.querySelectorAll('.cart-count').forEach((counter) => {
            counter.textContent = quantity;
        });
        cartTotal.replaceChildren(document.createTextNode(formatPrice(sum) + ' '));
        const currency = document.createElement('small');
        currency.textContent = "so'm";
        cartTotal.append(currency);

        if (!cart.size) {
            const message = document.createElement('p');
            message.className = 'cart-empty';
            message.append('Savatingiz hozircha bo‘sh.');
            message.append(document.createElement('br'));
            const hint = document.createElement('span');
            hint.textContent = 'Menyudan mazali tanlov qiling!';
            message.append(hint);
            cartItems.replaceChildren(message);
            return;
        }

        const rows = [...cart.entries()].map(([name, item]) => {
            const row = document.createElement('div');
            row.className = 'cart-row';
            const details = document.createElement('div');
            const title = document.createElement('strong');
            title.textContent = name;
            const price = document.createElement('small');
            price.textContent = `${formatPrice(item.price)} so'm`;
            details.append(title, price);

            const controls = document.createElement('div');
            controls.className = 'quantity-control';
            const decrease = document.createElement('button');
            decrease.type = 'button';
            decrease.textContent = '−';
            decrease.setAttribute('aria-label', `${name} sonini kamaytirish`);
            decrease.addEventListener('click', () => changeQuantity(name, -1));
            const count = document.createElement('span');
            count.textContent = item.quantity;
            const increase = document.createElement('button');
            increase.type = 'button';
            increase.textContent = '+';
            increase.setAttribute('aria-label', `${name} sonini oshirish`);
            increase.addEventListener('click', () => changeQuantity(name, 1));
            controls.append(decrease, count, increase);
            row.append(details, controls);
            return row;
        });
        cartItems.replaceChildren(...rows);
    };

    const changeQuantity = (name, amount) => {
        const item = cart.get(name);
        if (!item) return;
        item.quantity += amount;
        if (item.quantity <= 0) cart.delete(name);
        renderCart();
    };

    document.querySelectorAll('.add-button').forEach((button) => {
        button.addEventListener('click', () => {
            const { name, price } = button.dataset;
            const item = cart.get(name) || { price: Number(price), quantity: 0 };
            item.quantity += 1;
            cart.set(name, item);
            renderCart();
        });
    });

    const setCartOpen = (open) => {
        cartPanel.classList.toggle('open', open);
        cartPanel.setAttribute('aria-hidden', String(!open));
        cartButton.setAttribute('aria-expanded', String(open));
        cartOverlay.hidden = !open;
        document.body.classList.toggle('cart-open', open);
    };

    cartButton.addEventListener('click', () => setCartOpen(true));
    cartClose.addEventListener('click', () => setCartOpen(false));
    cartOverlay.addEventListener('click', () => setCartOpen(false));
    document.querySelector('.cart-menu-link').addEventListener('click', () => setCartOpen(false));
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') setCartOpen(false);
    });
})();
