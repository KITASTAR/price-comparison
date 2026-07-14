import streamlit as st

st.title("🛒 どっちがお得？比較アプリ")
st.write("パックAとパックBの価格と重さを入力して、どちらがお得か比較します。")

col1, col2 = st.columns(2)

with col1:
    st.subheader("パック A")
    price_a = st.number_input("価格 (円)", min_value=0, value=100, key="price_a")
    weight_a = st.number_input("容量 (g)", min_value=1, value=100, key="weight_a")
    per_100g_a = (price_a / weight_a) * 100
    st.metric(label="100gあたり", value=f"{per_100g_a:.1f} 円")

with col2:
    st.subheader("パック B")
    price_b = st.number_input("価格 (円)", min_value=0, value=100, key="price_b")
    weight_b = st.number_input("容量 (g)", min_value=1, value=100, key="weight_b")
    per_100g_b = (price_b / weight_b) * 100
    st.metric(label="100gあたり", value=f"{per_100g_b:.1f} 円")

st.divider()

if per_100g_a < per_100g_b:
    st.success(f"🏆 **パック A** の方がお得です！ (100gあたり {per_100g_b - per_100g_a:.1f} 円安い)")
elif per_100g_b < per_100g_a:
    st.success(f"🏆 **パック B** の方がお得です！ (100gあたり {per_100g_a - per_100g_b:.1f} 円安い)")
else:
    st.info("🤝 どちらも同じ価格（お得度）です！")
