"use client"

import { FormCheckbox, FormInput, OrangeButton } from "@/shared/components";
import { SpriteSVG } from "@/shared/img/SpriteSVG";
import { useFormik } from "formik";
import Link from "next/link";
import * as Yup from 'yup';

export default function SigninForm () {
  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
      rememberMe: false,
    },
    validationSchema: Yup.object().shape({
      email: Yup.string()
        .email('Дані введені некоректно')
        .required("Обов'язкова наявність електронної пошти"),
      password: Yup.string()
        .min(8, 'Пароль повинен мати довжину не менше 8 символів')
        .required('Потрібен пароль'),
      rememberMe: Yup.boolean(),
    }),
    onSubmit: async values => {
      console.log(values);
    },
  });

  return (
    <div>
      <form
        className="flex flex-col max-w-[400px] mx-auto gap-5"
        onSubmit={formik.handleSubmit}
      >
        <FormInput
          formik={formik}
          id="email"
          label={'Електронна пошта'}
          inputType="email"
        />

        <FormInput
          formik={formik}
          id="password"
          label={'Пароль'}
          inputType="password"
        />
        <div className="flex justify-between">
          <FormCheckbox
            formik={formik}
            id="rememberMe"
            label="Запам’ятати мене"
          />
          <Link href="/signin-forgot" className="text-blue-900">
            Нагадати пароль
          </Link>
        </div>

        <div className="w-28 mt-10 mx-auto pb-6">
          <OrangeButton onClick={() => {}} type="submit">
            Увійти
          </OrangeButton>
        </div>
      </form>

      <p className="text-center pb-3">Або увійдіть за допомогою:</p>
      <div className="flex justify-center pb-3">
        <SpriteSVG name="icon_google" />
      </div>
      <div className="flex justify-center">
        <p className="pr-6">Немає профілю?</p>
        <Link href="/signup" className="text-blue-90">
          Зареєструйся
        </Link>
      </div>
    </div>
  )
}