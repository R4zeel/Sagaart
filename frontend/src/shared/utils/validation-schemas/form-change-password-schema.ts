import * as yup from 'yup';

const schema = yup.object().shape({
	newPassword: yup
		.string()
		.required('Поле обязательно для заполнения')
		.min(8, 'Длина поля от 8 до 20 символов')
		.max(20, 'Длина поля от 8 до 20 символов')
		.matches(
			/[a-zA-Zа-яА-Я0-9!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~\u2116\u0024\u20AC\u00A3\u00A5\u20BD\u00A9\u2122\u00AE]$/,
			'Проверьте правильность ввода'
		),

	repeatNewPassword: yup
		.string()
		.required('Поле обязательно для заполнения')
		.min(8, 'Проверьте правильность ввода')
		.max(20, 'Проверьте правильность ввода')
		.matches(
			/[a-zA-Zа-яА-Я0-9!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~\u2116\u0024\u20AC\u00A3\u00A5\u20BD\u00A9\u2122\u00AE]$/,
			'Проверьте правильность ввода'
		)
		.oneOf([yup.ref('newPassword')], 'Пароль не совпадает с введенным'),
});
export default schema;